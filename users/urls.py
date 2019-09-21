from django.urls import path, include
from rest_framework import routers

from users import views

router = routers.DefaultRouter()
router.register(r'advertisers', views.AdvertiserUserViewSet)
router.register(r'users', views.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
