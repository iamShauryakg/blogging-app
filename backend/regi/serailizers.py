from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'Dob', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['email'] = validated_data['email'].lower()
        return CustomUser.objects.create_user(
            password=password,
            **validated_data
        )


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["login"],
            password=data["password"]
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data
