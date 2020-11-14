from django.urls import path, include
from . import views as v
from rest_framework import routers

app_name = 'cats'
router = routers.DefaultRouter()
router.register(r'cats', v.CatViewSet)
router.register(r'imgs', v.CatImagesViewSet)

urlpatterns = [
    path('',v.index, name="index"),
    path('adopt',v.adopt, name="adopt"),
    path('donate',v.donate, name="donate"),
    path('volunteer',v.volunteer, name="volunteer"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cats/',v.cats_list, name="cats_list"),
    path('test/',v.CatList, name="test"),
    path("catslist/", v.CatList.as_view(), name="catslist"),
    path("cats/<int:pk>/",v.CatDetail.as_view(),name='cat')
]




