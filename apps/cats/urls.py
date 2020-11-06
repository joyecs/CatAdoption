from django.urls import path
from . import views as v

app_name = 'cats'
urlpatterns = [
    path('',v.index, name="index"),
    path('adopt',v.adopt, name="adopt"),
    path('donate',v.donate, name="donate"),
    path('volunteer',v.volunteer, name="volunteer"),
]
