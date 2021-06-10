from django.contrib import admin

# Register your models here.
from .models import Tasks,User

admin.site.register(Tasks)
admin.site.register(User)