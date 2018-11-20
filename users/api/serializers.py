from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    viewed_house = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'department',
            'viewed_house',
        )

    def get_viewed_house(self, obj):
        return [house.name for house in obj.viewed_houses.all()]


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    username = serializers.CharField()
    # username = serializers.SerializerMethodField()
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile', 'is_superuser')


class SigninSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    remember = serializers.NullBooleanField(default=False)


class SignUpSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    department = serializers.IntegerField(default=-1)
    remember = serializers.NullBooleanField(default=False)
