from distance.models import Distance
from housing.models import House
from department.models import Department
from serializers import DistanceSerializer
from housing.api.serializers import HouseSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class DistanceViewSet(viewsets.ModelViewSet):
    model = Distance
    serializer_class = DistanceSerializer
    queryset = ''

    def list(self, request):
        queryset = Distance.objects.raw('SELECT * FROM distance_distance')
        serializers = DistanceSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        queryset = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.id = %s',[pk])
        serializers = DistanceSerializer(queryset, many=True)
        return Response(serializers.data)

class ClosestHouseViewSet(viewsets.ModelViewSet):
    model = House
    serializer_class = HouseSerializer
    queryset = ''

    def retrieve(self, request, pk):
        sql_query = (
            'SELECT housing_house.* FROM housing_house'
            ' INNER JOIN distance_distance ON housing_house.id = distance_distance.house_id_id'
            ' WHERE distance_distance.department_id_id = %s ORDER BY distance_distance.distance ASC, housing_house.price ASC'
        )

        queryset = House.objects.raw(sql_query,[pk])
        serializers = HouseSerializer(queryset, many=True)
        return Response(serializers.data)


