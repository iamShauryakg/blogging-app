from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import CustomUser


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            customUser = CustomUser.objects.get(
                Q(email=username) | Q(username=username)
            )
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return customUser
        return None
    