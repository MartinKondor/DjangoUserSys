import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import User
from contact.models import Contact


def _get_user_context_by_id(request, id):
    try: 
        user = User.objects.get(id=id)
    except:
        return HttpResponseNotFound(f"User with id={id}, cannot be found")
    return {
        "current_user": request.session.get("current_user"),
        "user": user,
        "user_fields": [f.name for f in User._meta.get_fields()],
        "contact_fields": [f.name for f in Contact._meta.get_fields()],
    }


def user(request, id):
    ctx = _get_user_context_by_id(request, id)
    return render(request, "user/user.html", ctx)

def users(request):
    return render(request, "user/users.html", {
        "current_user": request.session.get("current_user"),
        "users": User.objects.all(),
        "user_fields": [f.name for f in User._meta.get_fields()]
    })

def my_profile(request):
    user = json.loads(request.session.get("current_user"))
    ctx = _get_user_context_by_id(request, user["id"])
    return render(request, "user/my_profile.html", ctx)
