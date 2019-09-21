from rest_framework import viewsets

from users.models import AdvertiserUser, CustomUser
from users.serializers import AdvertiserUserSerializer, CustomUserSerializer


class AdvertiserUserViewSet(viewsets.ModelViewSet):
    queryset = AdvertiserUser.objects.all().order_by('name')
    serializer_class = AdvertiserUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('first_name')
    serializer_class = CustomUserSerializer
