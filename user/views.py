from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User


def user(request):
    return render(request, "user/user.html", {})

def users(request):
    return render(request, "user/users.html", {
        "users": User.objects.all(),
        "user_fields": [f.name for f in User._meta.get_fields()]
    })
