from rest_framework import viewsets,status
from users.models import UserProfile
from django.contrib.auth.models import User, BaseUserManager
from users.api.paginations import UserPagination
from users.api.serializers import UserSerializer, UserProfileSerializer, SigninSerializer, SignUpSerializer
from users.api.service import UserService
from users.api.permissions import UserPermission
from rest_framework import permissions
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login as django_login, logout as django_logout
from django.utils import timezone
from department.models import Department
from housing.models import House
from housing.api.serializers import HouseSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    pagination_class = UserPagination
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class UserViewset(viewsets.ModelViewSet):
    pagination_class = UserPagination
    serializer_class = UserSerializer
    permission_classes = (UserPermission, IsAuthenticated)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    @list_route(methods=['GET'])
    def profile(self, request):
        return Response(self.get_serializer(request.user).data)

    @list_route(methods=['GET'], permission_classes=[IsAuthenticated,])
    def suggestion(self, request):

        """ Advanced function 1 - House Suggestion:

            Sample query:
            Subquery A, close houses: SELECT * FROM housing_house WHERE closest_department_float = 34 AND id = user.department.id
            Subquery B, hot houses : SELECT * FROM housing_house WHERE id IN
                (SELECT housing_house.id FROM housing_house JOIN like_like ON housing_house.id = like_like.house_id_id GROUP BY housing_house.id HAVING count(*) >=3)
            Subquery C, cheap houses: SELECT * FROM housing_house WHERE price < 600

            Result query(suggested houses fitting 2 or more rules):
                (A INTERSECT B) UNION (A INTERSECT C) UNION (B INTERSECT C)
        """
        user = request.user
        if user.profile:
            closest_house_query = 'closest_department_float = %s' % user.profile.department.id
        else:
            closest_house_query = 'housing_house.id = -1'
        cheap_house_query = 'price < 600'
        hot_house_query = 'housing_house.id IN (SELECT housing_house.id FROM housing_house JOIN like_like ON housing_house.id = like_like.house_id_id AND like_like.has_liked=TRUE GROUP BY housing_house.id HAVING count(*) >=3)'
        hot_house_queryset = House.objects.extra(where=[hot_house_query])
        cheap_house_queryset = House.objects.extra(where=[cheap_house_query])
        closest_house_queryset = House.objects.extra(where=[closest_house_query])
        hot_cheap_house_queryset = hot_house_queryset & cheap_house_queryset
        hot_cheap_id = [house.id for house in hot_cheap_house_queryset]
        hot_close_house_queryset = hot_house_queryset & closest_house_queryset
        hot_close_id = [house.id for house in hot_close_house_queryset]
        cheap_close_house_queryset = cheap_house_queryset & closest_house_queryset
        cheap_close_id = [house.id for house in cheap_close_house_queryset]
        result_queryset = hot_close_house_queryset | hot_cheap_house_queryset | cheap_close_house_queryset
        data = HouseSerializer(result_queryset, many=True).data[:6]
        for house in data:
            if house["id"] in hot_cheap_id:
                house["suggested_reason"] = ["hot house", "cheap house"]
                continue
            if house["id"] in hot_close_id:
                house["suggested_reason"] = ["hot house", "close to your department"]
                continue
            if house["id"] in cheap_close_id:
                house["suggested_reason"] = ["cheap house", "close to your department"]
        return Response(data)

    @list_route(methods=['GET'])
    def roommate(self, request):

        """ Advanced function 2 - Potential Roommates
            Find 2 users from a same department and have both liked 3 or more same houses.

            Sample query:
            SELECT user_id FROM users_userprofile WHERE
            department_id = 34 AND
            user_id != 1 AND
            (SELECT count(*) FROM ((SELECT house_id_id FROM like_like WHERE user_id_id = user_id AND has_liked = TRUE)
              INTERSECT
            (SELECT house_id_id FROM like_like WHERE user_id_id = 1 AND has_liked = TRUE)) as same) >= 3;
        """

        user = request.user
        if not user.profile:
            return None
        user_department_id = user.profile.department_id
        roommate_query = 'SELECT * FROM users_userprofile WHERE department_id = %s AND user_id != %s AND' % (user_department_id, user.id)
        user_like_query = '(SELECT house_id_id FROM like_like WHERE user_id_id = %s AND has_liked = TRUE)' % user.id
        roommate_like_query = '(SELECT house_id_id FROM like_like WHERE user_id_id = user_id AND has_liked = TRUE)'
        judge_query = '(SELECT count(*) FROM (%s INTERSECT %s) AS same) >= 3' % (user_like_query, roommate_like_query)
        roommate_query = roommate_query + judge_query
        user_queryset = UserProfile.objects.raw(roommate_query)
        return Response([UserSerializer(profile.user).data for profile in user_queryset])

    @list_route(methods=['GET'])
    def logout(self, request):
        django_logout(request)
        return Response({'next': '/'}, status=status.HTTP_200_OK)

    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def signin(self, request):
        serializer = SigninSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username_or_email = serializer.data['username_or_email']
        password = serializer.data['password']
        user = UserService.get_user_by_username_or_email(username_or_email)
        if not user:
            error = 'Username or email does not exist.'
            return Response({'error': error}, status=status.HTTP_401_UNAUTHORIZED)

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        django_login(request, user)
        remember = serializer.data['remember']
        if not remember:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(60 * 60 * 24 * 60)

        next = request.GET.get('next', '')
        if next == '':
            next = '/problem/'
        return Response({'next': next}, status=status.HTTP_200_OK)

    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def signup(self, request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.data['email']
        password = serializer.data['password']
        username = serializer.data['username']
        department_id = serializer.data['department']
        email = BaseUserManager.normalize_email(email)
        user = UserService.get_user_by_username_or_email(email)
        if user:
            return Response({'error': "Email has been used"}, status=status.HTTP_401_UNAUTHORIZED)
        now = timezone.now()
        user = User.objects.create(email=email, username=username,
                                   is_staff=False, is_superuser=False, is_active=True,
                                   last_login=now, date_joined=now)
        user.set_password(password)
        profile = UserProfile.objects.create(user=user)
        if department_id:
            depart = Department.objects.get(id=department_id)
            profile.department = depart

        user.save()
        profile.save()
        return Response({'message': 'Create user successfully'}, status=status.HTTP_200_OK)

