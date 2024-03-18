from django.urls import path

from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("users", views.users, name="users"),
]
