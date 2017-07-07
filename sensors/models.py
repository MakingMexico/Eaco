from django.db import models
from users.models import *


class Sensor(models.Model):
    # Owner info
    owner = models.ForeignKey(Client, null=True, blank=True)
    # Sensor info
    serial = models.CharField(max_length=13)
    # Sensor catched info
    temperature = models.IntegerField(null=True, blank=True)
    digital_light = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
