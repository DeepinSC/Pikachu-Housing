from rest_framework import serializers
from housing.models import House
from distance.models import Distance
from rest_framework.response import Response
from django.http import JsonResponse
from department.api.serializers import DepartmentSerializer
from like.models import Like

class HouseSerializer(serializers.ModelSerializer):

    closest_department = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    user_like = serializers.SerializerMethodField()

    def get_closest_department(self, obj):

        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])
        
        for item in distance_set:
            serializer = DepartmentSerializer(item.department_id)
            serialized_data = serializer.data
            serialized_data['distance'] = item.distance
            return serialized_data

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id = obj.id, has_liked = True).count()
        return count

    def get_user_like(self, obj):
        request = self.context.get("request")
        if (request.auth is None):
            return False
        else:
            user_id = request.user
            return Like.objects.filter(user_id = user_id, house_id = obj.id, has_liked = True).exist()

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
            'like_count',
            'user_like'
        )
