from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'age', 'color',  'image' )  
    # list_filter = ('breed')

@admin.register(Cat_images)
class ImgsAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
# admin.site.register(Cat)
# admin.site.register(Cat_images)

