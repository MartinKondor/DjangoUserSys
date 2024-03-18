from django.db import models
from django.conf import settings
from django.utils import timezone


class Contact(models.Model):
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=200, null=True)
    notes = models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.phone}, {self.email}'
