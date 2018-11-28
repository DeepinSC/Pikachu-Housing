from rest_framework import serializers
from housing.models import House
from distance.models import Distance
from department.models import Department
from department.api.serializers import DepartmentSerializer
from provider.api.serializers import ProviderSerializer
from like.models import Like


class HouseSerializer(serializers.ModelSerializer):
    closest_department = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    provider = ProviderSerializer(required=False, allow_null=True)

    def get_closest_department(self, obj):
        department_set = Department.objects.raw('SELECT * FROM department_department WHERE id = %s', [int(obj.closest_department_float)])
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])
        
        for item in department_set:
            serializer = DepartmentSerializer(item)
            serialized_data = serializer.data

        for item in distance_set:
            serialized_data['distance'] = item.distance
            return serialized_data

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id=obj.id, has_liked=True).count()
        return count

    def get_has_liked(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated():
            return False
        else:
            user_id = request.user
            return Like.objects.filter(user_id=user_id, house_id=obj.id, has_liked=True).exists()
          
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
            'has_liked'
        )
