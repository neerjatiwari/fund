from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "basicfund/index.html")

def profile(request):
    return render(request, "basicfund/profile.html", {"name": "Neerja"})

def login(request):
    return render(request, "basicfund/login.html")

def join(request):
    return render(request, "basicfund/join.html")

def about(request):
    return render(request, "basicfund/about.html")

def kristina(request):
    return render(request, "basicfund/kristina.html")

def donate1(request):
    return render(request, "basicfund/donate.html")

def domi(request):
    return render(request, "basicfund/domi.html")

def lynsey(request):
    return render(request, "basicfund/lynsey.html")

def marie(request):
    return render(request, "basicfund/marie.html")

def stuart(request):
    return render(request, "basicfund/stuart.html")


