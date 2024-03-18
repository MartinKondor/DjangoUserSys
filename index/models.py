from django.db import models
from django.conf import settings
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password_hash = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    contact_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.contact_id}, {self.created_date}'
