from rest_framework import serializers
from .models import *

class AdopterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adopter
        fields = ('id', 'name', 'phone', 'email', 'address', 'an_income', 'reasons')