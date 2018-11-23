from rest_framework import viewsets, status
from like.models import Like
from like.api.paginations import LikePagination
from serializers import LikeSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from housing.models import House


@permission_classes((IsAuthenticatedOrReadOnly,))
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    pagination_class = LikePagination
    serializer_class = LikeSerializer

    def create(self, request):
        serializer = LikeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_id = serializer.data['user_id']
        user = get_object_or_404(User, id=user_id)
        house_id = serializer.data['house_id']
        house = get_object_or_404(House, id=house_id)
        if Like.objects.filter(user_id = user_id, house_id=house_id).exists():
            obj = Like.objects.get(user_id=user_id, house_id=house_id)
            obj.has_liked = not obj.has_liked
            obj.save()
            return Response(status=status.HTTP_201_CREATED, data={'like': obj.has_liked})
        else:
            new_like = Like.objects.create(user_id = user, house_id=house, has_liked=True)
            new_like.save()
            return Response(status=status.HTTP_202_ACCEPTED, data={'like': new_like.has_liked})
