from django.urls import path, include
from . import views as v
from rest_framework import routers

app_name = 'cats'
router = routers.DefaultRouter()
router.register(r'', v.CatViewSet)
urlpatterns = [
    path('',v.index, name="index"),
    path('adopt',v.adopt, name="adopt"),
    path('donate',v.donate, name="donate"),
    path('volunteer',v.volunteer, name="volunteer"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]




