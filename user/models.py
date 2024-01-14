from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, username: str, password: str = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, email: str, username: str, password: str) -> "User":
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
