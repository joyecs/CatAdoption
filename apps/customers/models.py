from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    annual_income = models.IntegerField(null=True, blank=True)
    reason_to_adopt_cats = models.CharField(max_length=800)