from django.urls import path
from .api_views import PostListAPI, PostDetailAPI

urlpatterns = [
    path("posts/", PostListAPI.as_view()),
    path("posts/<slug:slug>/", PostDetailAPI.as_view())

]