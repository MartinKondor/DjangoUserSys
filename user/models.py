from django.db import models
from django.conf import settings
from django.utils import timezone

from index.forms import SignUpForm
from contact.models import Contact


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password_hash = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    @staticmethod
    def from_form(form: SignUpForm) -> models.Model:
        """
        Generate a User object form the signup form
        """
        u = User()
        for field in [f.name for f in User._meta.get_fields()]:

            if field == "password_hash":
                # TODO: encode password
                u.password_hash = form.data.get("password")
                continue
            
            value = form.data.get(field)
            if value:
                u.__setattr__(field, value)
        return u

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.created_date}'
