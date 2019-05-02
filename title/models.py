from django.db import models
from django.db.models import Q


# Create your models here.

class Title(models.Model):
    asin = models.CharField(max_length=120, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    publisher = models.CharField(max_length=120, blank=True, null=True)
    marketingservices = models.CharField(max_length=120, blank=True, null=True)
    batch = models.CharField(max_length=120, blank=True, null=True)
