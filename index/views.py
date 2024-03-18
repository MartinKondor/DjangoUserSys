from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import check_password, make_password

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
    
        if form.data.get('password') != form.data.get('password_again'):
            return render(request, "index/signup.html", send_error("The passwords doesn't match", context))
    
        # Check if the email is already registered
        if Contact.objects.filter(email__contains=form.data.get("email")).first() is not None:
            return render(request, "index/signup.html", send_error("This email is already registered, please try another one", context))

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
    error_msg = "Wrong email or password"

    if request.method == "POST":
        form = SignInForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(request, "index/signin.html", send_error(error_msg, context))
    
        # Get the contact related to the email
        contact = Contact.objects.filter(email__contains=form.data.get('email')).first()
        if contact is None:
            print("1.")
            return render(request, "index/signin.html", send_error(error_msg, context))

        # Get the user related to the contact
        user = User.objects.filter(contact=contact).first()
        if user is None:
            print("2.")
            return render(request, "index/signin.html", send_error(error_msg, context))

        # Check password
        if User.check_password(form.data.get('password'), user.password_hash):
            print("3.")
            return render(request, "index/signin.html", send_error(error_msg, context))

        context = send_success("You've signed in!", context)
        return render(request, "index/index.html", context)
    
    return render(request, "index/signin.html", {"form": SignInForm()})


def signout(request):
    # TODO: Sign out user and redirect to the home page
    return redirect("/")
