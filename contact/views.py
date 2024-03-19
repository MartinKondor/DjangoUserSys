from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Contact


def contact(request, id):
    try: 
        contact = Contact.objects.get(id=id)
    except:
        return HttpResponseNotFound(f"Contact with id={id}, cannot be found")
    return render(request, "contact/contact.html", {
        "current_user": request.session.get("current_user"),
        "contact": contact,
        "contact_fields": [f.name for f in Contact._meta.get_fields()],
    })


def contacts(request):
    return render(request, "contact/contacts.html", {
        "current_user": request.session.get("current_user"),
        "contacts": Contact.objects.all(),
        "contact_fields": [f.name for f in Contact._meta.get_fields() if f.name!="user"]
    })
