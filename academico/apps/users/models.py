from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserMananger(BaseUserManager, models.Manager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('EL email debe ser obligatorio')
        user = self.model(username = username, email=email, is_active= True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save( using = self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class User (AbstractBaseUser, PermissionsMixin):
    username  = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length= 100)
    avatar = models.ImageField(upload_to = 'users')# fatal hacer algo

    objects = UserMananger()

    is_active = models.BooleanField(default=True)
    is_staff = models.NullBooleanField(default= False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def get_short_name(self):
        return self.username
