from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Customer)
@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'address', 'an_income', 'reasons')
