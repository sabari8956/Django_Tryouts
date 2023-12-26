from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login,authenticate
from django.urls import reverse
from django.db import IntegrityError
from .models import *
# Create your views here.

def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        # confirmation = request.POST["confirmation"]
        file = request.FILES.get('profile_img')
        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username , email=email, password=password, profile_img=file)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "register.html", {
                "message": "username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "login.html")
