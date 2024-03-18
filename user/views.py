from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def user(request):
    return HttpResponse("user")

def users(request):
    return HttpResponse("users")
