from django.shortcuts import render

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