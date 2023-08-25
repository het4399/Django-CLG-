from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def home(request):
    movies=Movie.object.all()
    searchTerm1=request.GET.get("searchMovie")
    return render(request,'index.html',{"searchTerm":searchTerm1,'movies':movies})

def about(request):
    return HttpResponse('<h2>About Us </h2>')
def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{"email":email})