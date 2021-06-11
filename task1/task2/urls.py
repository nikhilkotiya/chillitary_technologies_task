from .import views
from django.urls import path,include
urlpatterns = [
    path('task2',views.task,name="task")
]