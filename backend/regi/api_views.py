from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serailizers import LoginSerializer, RegisterSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customUser = serializer.save()

        return Response({
            'id': customUser.id,
            'username': customUser.username,
            'email': customUser.email
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customUser = serializer.validated_data['customUser']

        return Response({
            'id': customUser.id,
            'username': customUser.username,
            'email': customUser.email
        }, status=status.HTTP_200_OK)
    

