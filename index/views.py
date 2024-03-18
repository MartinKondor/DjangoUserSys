from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index")

def signup(request):
    return HttpResponse("signup")

def signin(request):
    return HttpResponse("signin")

def signout(request):
    return HttpResponse("signout")
