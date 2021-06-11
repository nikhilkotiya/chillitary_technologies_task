from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .manager import MyUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=20,unique=True)
    join_date= models.DateTimeField(default=timezone.now)
    password=models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

class Tasks(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    task_title=models.CharField(max_length=200)
    task_description=models.CharField(max_length=2000,null=True)
    task_pic=models.FileField(upload_to="images", null=True, blank=True)
    date=models.DateTimeField(default=timezone.now)