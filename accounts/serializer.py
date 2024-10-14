from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "get_full_name",
            "username",
            "email",
            "last_login",
            "date_joined",
        ]


class BaseCartWishlistUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "get_full_name"]
