from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import *
from .models import *


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer