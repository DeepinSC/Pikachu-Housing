from rest_framework import serializers
from like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user_id',
            'house_id',
            'has_liked',
        )
