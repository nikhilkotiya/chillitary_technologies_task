from django.shortcuts import render
from .models import Table
# Create your views here.
def task(request):
    data=Table.objects.all()
    return render(request,"all_data.html" ,{"x":data})