from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Ale(request):
    return HttpResponse("Hello, Ale!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })