from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def contact(request, id):
    return render(request, "contact/contact.html", {})


def contacts(request):
    return render(request, "contact/contacts.html", {})
