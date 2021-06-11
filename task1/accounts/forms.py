from django.contrib.auth.forms import UserCreationForm
from .models import User,Tasks
from django import forms

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)

class TaskF(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'