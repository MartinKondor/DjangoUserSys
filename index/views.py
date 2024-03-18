from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from UserSys.utils import send_error, send_success
from .forms import SignInForm


def index(request):
    return render(request, "index/index.html", {})


def signup(request):
    if request.method == "POST":
        pass
    return render(request, "index/signup.html", {})


def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            context = send_error("Wrong email or password", context)
            return render(request, "index/signin.html", context)
    
        # context = send_success("You've signed in!")
    
    form = SignInForm()
    context = {"form": form}
    return render(request, "index/signin.html", context)


def signout(request):
    # Sign out user and redirect to the home page
    return redirect("/")
