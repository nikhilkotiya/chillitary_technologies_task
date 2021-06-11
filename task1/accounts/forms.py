from django.contrib.auth.forms import UserCreationForm
from .models import User,Tasks
from django import forms
from django.core.exceptions import ValidationError
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)

def usernamevalidator(use):
    a=use[-1:]
    print(a)
    if((a=='1') or (a=='0')):
        return True 
    return False
def usernamefvalidator(use):
    b=use[:1]
    print(b)
    if((b=='a')or(b=="A")):
        return True
    return False
class UserF(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
    # def checkusername(self):
    #     a=self.username[-1:]
    #     b=self.username[1:]
    #     if((a!=1) or (a!=0)):
    #         raise forms.ValidationError("Last letter should be end with 1/0")
        
        
    #     if((b!="A") or (b!='a')):
    #         raise forms.ValidationError("letter should be satrt with a/A")
    #     return self.username
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

    