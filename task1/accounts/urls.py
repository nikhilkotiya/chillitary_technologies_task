from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
# from . views import SignUpView
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('task/',views.task,name="task"),
    path('all_data/',views.tasks,name="all_data")
]
 