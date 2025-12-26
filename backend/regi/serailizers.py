from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'Dob', 'password']

    def validate(self,data):
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use"})
        if CustomUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "Username is already in use"})
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        customUser = CustomUser(**validated_data)
        customUser.set_password(password)
        customUser.save()
        return customUser    



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