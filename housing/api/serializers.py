from rest_framework import serializers
from housing.models import House
from distance.models import Distance
from department.models import Department
from rest_framework.response import Response
from django.http import JsonResponse
from department.api.serializers import DepartmentSerializer
from like.models import Like

class HouseSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    closest_department = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id = obj.id).count()
        return count

    def get_closest_department(self, obj):
        department_set = Department.objects.raw('SELECT * FROM department_department WHERE id = %s', [int(obj.closest_department_float)])
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])
        
        for item in department_set:
            serializer = DepartmentSerializer(item)
            serialized_data = serializer.data

        for item in distance_set:
            serialized_data['distance'] = item.distance
            return serialized_data

    class Meta:
        model = House
        fields = (
            'id',
            'name',
            'price',
            'location',
            'cover_img',
            'types',
            'description',
            'imgs_url',
            'latitude',
            'longitude',
            'provider',
            'closest_department',
            'like_count'
        )
