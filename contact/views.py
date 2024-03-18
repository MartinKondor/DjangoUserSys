from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    return HttpResponse("contact")

def contacts(request):
    return HttpResponse("contacts")
