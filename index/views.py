from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from UserSys.utils import send_error, send_success
from .forms import SignInForm, SignUpForm
from user.models import User
from contact.models import Contact


def index(request):
    return render(request, "index/index.html", {})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(
                request,
                "index/signup.html",
                send_error(form.errors[0], context)
            )
    
        if form.data['password'] != form.data['password_again']:
            return render(request, "index/signup.html", send_error("The passwords doesn't match", context))
    
        # Sign up the user and make a contact for it
        # delete the object if there is an error
        user = User.from_form(form)
        contact = Contact.from_form(form)
        try:
            contact.save()
            user.contact = contact
            user.save()
        except:
            try: user.delete()
            except: pass
            try: contact.delete()
            except: pass

        context = send_success("You've signed up!", context)
        return render(request, "index/index.html", context)

    return render(request, "index/signup.html", {"form": SignUpForm()})


def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(
                request,
                "index/signin.html",
                send_error("Wrong email or password", context)
            )
    


        context = send_success("You've signed in!", context)
        return render(request, "index/index.html", context)
    
    return render(request, "index/signin.html", {"form": SignInForm()})


def signout(request):
    # TODO: Sign out user and redirect to the home page
    return redirect("/")
