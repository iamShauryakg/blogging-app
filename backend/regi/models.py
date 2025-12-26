from django.db import models

from django.contrib.auth.models import abstractBaseUser, PermissionsMixin
from .managers  import CustomUserManager



class CustomUser(abstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Dob = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    

    USERNAME_FIELD = ['email', 'username']
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'Dob']

    def __str__(self):
        return self.username