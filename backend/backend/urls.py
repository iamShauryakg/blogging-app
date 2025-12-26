
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("regi.urls")),
    path("api/", include("blog.urls")),
]
