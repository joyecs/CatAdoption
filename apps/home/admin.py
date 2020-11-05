from django.contrib import admin
from django.contrib.auth.models import Group


# admin.site.site_title = 'site title'
# admin.site.site_header = 'site header'

admin.site.unregister(Group)
