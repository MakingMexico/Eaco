from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    # User info
    user = models.OneToOneField(User)
    # Contact info
    celphone = models.PhoneNumberField()
    # Meta data
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
