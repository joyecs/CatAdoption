from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import *
from .models import Cat
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    # return HttpResponse('index')
    html = 'cats/index.html'
    return render(request, html)
@csrf_exempt    
def cats_list(request):
    if request.method == 'GET':
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        context = {

        }
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CatSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

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
# show cats    
class CatList(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'cats/adopt.html'
    # cat list    
    def get(self,request):
        queryset = Cat.objects.all()
        serializer = CatSerializer(queryset, many=True)
        # return Response({})
        return Response({'cats':serializer.data})
        # return Response({'cats':"收到后三地"})
    def post(self,request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            cat_saved = serializer.save()
            return Response({"success": "Cat '{}' created successfully!".format(cat_saved.name)})  
        return Response({"Error":serializer.errors})  

class CatDetail(APIView):
    def get_object(self,pk):
        try:
            return Cat.objects.get(pk=pk)
        except Cat.DoesNotExist:
            raise Http404
    def get(self,request,pk, format=None):
        cat_ = self.get_object(pk)
        serializer = CatSerializer(cat_)
        return Response(serializer.data)    
    def put(self, request, pk, format=None):
        cat_ = self.get_object(pk)
        serializer = CatSerializer(cat_, data=request.data)
        if serializer.is_valid():
            cat_saved = serializer.save()     
            return Response({"success": "Cat '{}' updated successfully!".format(cat_saved.name)})    
        return Response({"Error": serializer.errors})  
    def delete(self,request,pk,format=None):
        cat_ = self.get_object(pk)
        cat_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
class CatImagesViewSet(viewsets.ModelViewSet):
    queryset = Cat_images.objects.all()
    serializer_class = CatImageSerializer