from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def contact(request):
    return HttpResponse("contact")


def contacts(request):
    return HttpResponse("contacts")
