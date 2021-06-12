from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
# Create your models here.
class Table(models.Model):
    title=models.CharField(max_length=20,unique=True,default="")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,default="",blank=True, related_name='children')
    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        ret = self.title
        return ret