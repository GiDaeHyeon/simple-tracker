import django
from django.db import models


class CarStatus(models.Model):
    name = models.CharField(null=False, max_length=128)
    ping = models.IntegerField(null=False)
    date_time = models.DateTimeField(null=False)
    key_on_datetime = models.DateTimeField(null=False)
    key_off_datetime = models.DateTimeField(null=False)
    speed = models.IntegerField(null=False)
    distance = models.FloatField(null=False)
    cum_distance = models.IntegerField(null=False)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
