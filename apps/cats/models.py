from django.db import models

# Create your models here.

class Cat(models.Model):
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="cat_images/%Y/%m/")