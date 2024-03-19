from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import User
from contact.models import Contact


def user(request, id):
    try: 
        user = User.objects.get(id=id)
    except:
        return HttpResponseNotFound(f"User with id={id}, cannot be found")
    return render(request, "user/user.html", {
        "user": user,
        "user_fields": [f.name for f in User._meta.get_fields()],
        "contact_fields": [f.name for f in Contact._meta.get_fields()],
    })

def users(request):
    return render(request, "user/users.html", {
        "users": User.objects.all(),
        "user_fields": [f.name for f in User._meta.get_fields()]
    })
