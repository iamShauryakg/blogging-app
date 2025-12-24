from .serializers import PostSerializer
from .models import Post

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class PostListAPI(generics.ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()

        return queryset

class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

    