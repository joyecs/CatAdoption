from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CatSerializer
from .models import Cat

# Create your views here.
def index(request):
    # return HttpResponse('index')
    html = 'cats/index.html'
    return render(request, html)

def adopt(request):
    # return HttpResponse('index')
    html = 'cats/adopt.html'
    return render(request, html)

def donate(request):
    # return HttpResponse('index')
    html = 'cats/donate.html'
    return render(request, html)

def volunteer(request):
    # return HttpResponse('index')
    html = 'cats/volunteer.html'
    return render(request, html)

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('breed')
    serializer_class = CatSerializer