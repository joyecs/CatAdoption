from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer