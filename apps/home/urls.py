from django.urls import path
from django.contrib import admin

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index,name='index'),
]

admin.site.site_header = 'FOSTER CAT'
admin.site.site_title = 'FOSTER CAT'
admin.site.index_title = 'FOSTER CAT'
# admin.site.login_template = 'login.html'
