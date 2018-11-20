from rest_framework import viewsets,status
from users.models import UserProfile
from django.contrib.auth.models import User, BaseUserManager
from users.api.paginations import UserPagination
from users.api.serializers import UserSerializer, UserProfileSerializer, SigninSerializer, SignUpSerializer
from users.api.service import UserService
from users.api.permissions import UserPermission
from rest_framework import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.utils import timezone
from department.models import Department


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

