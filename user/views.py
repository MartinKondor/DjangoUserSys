from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return HttpResponse("user")

def users(request):
    return HttpResponse("users")
