from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    searchTerm1=request.GET.get("searchMovie")
    return render(request,'index.html',{"searchTerm":searchTerm1})

def about(request):
    return HttpResponse('<h2>About Us </h2>')
def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{"email":email})