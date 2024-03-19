from django.db import models
from django.conf import settings
from django.utils import timezone

from UserSys.utils import JsonSerializable
from index.forms import SignUpForm
from contact.models import Contact
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model, JsonSerializable):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password_hash = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    @staticmethod
    def check_password(*args, **kwargs):
        return check_password(*args, **kwargs)

    @staticmethod
    def from_form(form: SignUpForm) -> models.Model:
        """
        Generate a User object form the signup form
        """
        u = User()
        for field in [f.name for f in User._meta.get_fields()]:

            if field == "password_hash":
                print(form.data.get("password"))
                u.password_hash = make_password(form.data.get("password"), settings.PASSWORD_SALT)
                continue
            
            value = form.data.get(field)
            if value:
                u.__setattr__(field, value)
        return u

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.created_date}'
