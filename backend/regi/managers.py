from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email is required")
        
        email = self.normalize_email(email)
        customUser = self.model(email=email, **extra_fields)
        customUser.set_password(password)
        customUser.save(using=self._db)
        return customUser
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)