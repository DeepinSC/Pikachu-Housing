from rest_framework import viewsets
from housing.models import House
from provider.models import Provider
from department.models import Department 
from distance.models import Distance 
from housing.api.paginations import HousePagination
from serializers import HouseSerializer
from rest_framework import permissions

class HouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
