from os.path import splitext
import datetime

from django.db import models

from apps.home.utils import get_random_str as rs

def _path(instance, filename):
    try: cl = str(type(instance).__name__)
    except: cl = 'cn'
    _, ext = splitext(filename)
    _now = datetime.datetime.today()
    return "uploads/{cl}/{year}/{month}/{rs}{ext}".format(year=_now.strftime("%Y"), 
        month=_now.strftime("%m"), cl=cl, rs=rs(15).lower(), ext=ext)
#>>>>>>end of _path

class Cat(models.Model):
    name = models.CharField(max_length=50, default='')
    breed = models.CharField(max_length=100, default='', blank=True)
    age = models.CharField(max_length=100, blank=True, default='')
    color = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True, null=True, upload_to=_path)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{},{}".format(self.name, self.breed)