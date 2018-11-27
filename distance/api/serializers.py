from rest_framework import serializers
from distance.models import Distance


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = (
            'house_id',
            'department_id',
            'distance',
        )
