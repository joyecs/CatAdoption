from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(r):
    return HttpResponse('index')

def handler404(r,exception):
    return render(r, 'home/404.html')

def handler500(r):
    return render(r, 'home/404.html')
