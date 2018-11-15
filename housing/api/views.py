from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import HouseSerializer
from rest_framework import permissions
from rest_framework.response import Response

class HouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    permission_classes = (permissions.BasePermission,)
    queryset = ''

    def list(self, request):
        queryset = House.objects.raw('SELECT * FROM housing_house')
        serializers = HouseSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        queryset = House.objects.raw('SELECT * FROM housing_house WHERE housing_house.id = %s',[pk])
        serializers = HouseSerializer(queryset, many=True)
        return Response(serializers.data)
