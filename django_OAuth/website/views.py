from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def index(request):
    
    return render(request, "index.html")

def logout_views(request):
    logout(request)
    return redirect("/")