from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    join_date= models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=30)

class Tasks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_title=models.CharField(max_length=200, validators=[MinLengthValidator(4)])
    task_description=models.CharField(max_length=2000,null=True)
    task_pic=models.FileField(upload_to="images")
    date=models.DateTimeField(auto_now_add=True)