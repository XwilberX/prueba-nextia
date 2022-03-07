from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name

class BienesModel(BaseModel):
    article = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)