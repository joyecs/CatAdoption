from django.db import models

# Create your models here.
class Adopter(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    an_income = models.IntegerField(null=True, blank=True)
    reasons = models.TextField(max_length=800, null=True, blank=True)