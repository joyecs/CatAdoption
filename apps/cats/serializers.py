from rest_framework import serializers
from .models import *

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'breed', 'age', 'color',  'image' )    
class CatImageSerializer(serializers.Serializer):
    cat = CatSerializer(required=True)
    class Meta:
        model = Cat_images
        fields = ('id', 'img')
