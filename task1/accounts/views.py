from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.44
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .models import User
from  .forms import SignUpForm,TaskF
from django.views.decorators.csrf import csrf_exempt
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
@csrf_exempt
def login_view(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            return redirect('/signup/')
        else:
            error="wrong username or password"
            return render(request,"login.html",{"e":error})
    return render(request,"login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponse("Hello, world. This is a logout page")

@csrf_exempt
def task(request):
    if request.method=="POST":
        form = TaskF(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            form.save()
            return HttpResponse('save')
    else:
        form = TaskF()
    return render(request, 'task.html', {'form': form})