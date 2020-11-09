from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email', 'address', 'annual_income', 'reason_to_adopt_cats')