"""fostercats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('apps.home.urls', namespace='home')),
    path('', include('apps.home.urls', namespace='index')),
    path('cats/', include('apps.cats.urls', namespace='cats')),
    path('customers/', include('apps.customers.urls'))
]

if settings.DEBUG == True:
    # urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == False:
    handler404 = 'apps.home.views.handler404'
    handler500 = 'apps.home.views.handler500'

# for test
if settings.DEBUG:
    urlpatterns += [
        url(r'^catimage/(?P<path>.*)$', serve, {
            'document_root': settings.CAT_ROOT,
        }),
    ]