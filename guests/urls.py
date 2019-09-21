from django.urls import path, include
from rest_framework import routers

from guests import views

router = routers.DefaultRouter()
router.register(r'guests', views.GuestsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]