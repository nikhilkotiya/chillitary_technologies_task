from django.contrib.auth.forms import UserCreationForm
from .models import User,Tasks
from django import forms
from django.core.exceptions import ValidationError
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)

class TaskF(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

    def clean_task_title(self):
        data=self.cleaned_data.get('task_title')
        if (len(data)< 10):
            print("1")
            raise forms.ValidationError(
                "task tile character must be greater then 10"
                )
        return data