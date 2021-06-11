from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.44
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .models import User,Tasks
from  .forms import SignUpForm,TaskF,UserF,usernamevalidator,usernamefvalidator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# class SignUpView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def signup(request):
    if request.method=="POST":
        if not User.objects.filter(username=request.POST["username"]).exists():
            use = request.POST["username"]
            print(usernamevalidator(use))
            if usernamevalidator(use) is False:
                context="Username should end with 1/0"
                return render(request,"signup.html",{"errorU":context})
            if  usernamefvalidator(use) is False:
                context="Username should start with a/A"
                return render(request,"signup.html",{"errorA":context})               
            if request.POST["password"]==request.POST["rpassword"]:
                if (len(request.POST["password"]) > 7):
                    data=User()
                    data.password=make_password(request.POST["password"])
                    data.username=request.POST["username"]
                    data.save()
                    print("user saved")
                    return redirect("/login")
                else:
                    context="Length must be greter then 8"
                    return render(request,"signup.html",{'errorP':context})
            else:
                context="Password confirmation doesn't match"
                print("wrong password")
                return render(request,"signup.html",{'errorPC':context})
        else:
            context="username Already Exist"
            return render(request,"signup.html",{'errorE':context})   
    else:
        return render(request,"signup.html")
@csrf_exempt
def login_view(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            return redirect('/task/')
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
            return redirect('/all_data')
    else:
        form = TaskF()
    return render(request, 'task.html', {'form': form})
def tasks(request):
    task=Tasks.objects.all().order_by("id")
    p = Paginator(task, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  
    # except PageNotAnInteger:
    #     page_obj = p.page(1)
    # except EmptyPage:  
    #     page_obj = p.page(p.num_pages)
    # context = {'page_obj': page_obj}
    return render(request,"tasks.html",{"Tasks":page_obj})