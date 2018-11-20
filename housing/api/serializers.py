from rest_framework import serializers
from housing.models import House


class HouseSerializer(serializers.ModelSerializer):
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
            'provider'
        )
