from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to home page</h1>')

def about(request):
    return HttpResponse('<h2>About Us </h2>')