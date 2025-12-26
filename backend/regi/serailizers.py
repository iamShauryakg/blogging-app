from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        customUser = authenticate(
            username=data["login"],
            password=data["password"]
        ) 
        if not customUser:
            raise serializers.ValidationError("Invalid login credentials")
        data["customUser"] = customUser
        return data