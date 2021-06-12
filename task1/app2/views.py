from django.shortcuts import render
from .models import Table
# Create your views here.
def data(request):
    return render(request, "index.html", {'data': Table.objects.all()})
