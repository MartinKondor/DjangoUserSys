from django.db import models
from django.conf import settings
from django.utils import timezone

from UserSys.utils import JsonSerializable
from index.forms import SignUpForm


class Contact(models.Model, JsonSerializable):
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=200, null=True)
    notes = models.TextField(null=True)

    @staticmethod
    def from_form(form: SignUpForm) -> models.Model:
        """
        Generate a Contact object form the signup form
        """
        c = Contact()
        for field in [f.name for f in Contact._meta.get_fields()]:
            value = form.data.get(field)
            if value:
                c.__setattr__(field, value)
        return c

    def __str__(self) -> str:
        return f'{self.phone}, {self.email}, {self.notes}'
