from django.urls import path, include
from rest_framework import routers

from adverts import views

router = routers.DefaultRouter()
router.register(r'adverts', views.AdvertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
