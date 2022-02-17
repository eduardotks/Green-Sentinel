from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    potency = models.CharField(max_length=5)
    duration = models.IntegerField()
    serial = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
