from django.urls import path

from . import views

urlpatterns = [
    path("my_profile", views.my_profile, name="my_profile"),
    path("users", views.users, name="users"),
    path("<slug:id>", views.user, name="user"),
]
