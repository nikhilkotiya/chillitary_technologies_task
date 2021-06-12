from django.shortcuts import render
from .models import Genre
# Create your views here.
def show_genres(request):
    return render(request, "index.html", {'genres': Genre.objects.all()})
