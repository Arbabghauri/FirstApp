from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login  # Add login here
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")


def Aboutme(request):
    return render(request, "Aboutme.html")


from django.shortcuts import render, redirect


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)

            return redirect("dashboard")
        # Email verification

    else:
        form = SignupForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


from django.contrib.auth import logout


# logout page
def user_logout(request):
    logout(request)
    return redirect("/")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")
