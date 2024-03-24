from django.contrib import admin

from contact.models import Contact
from user.models import User


admin.site.register(User)
admin.site.register(Contact)
