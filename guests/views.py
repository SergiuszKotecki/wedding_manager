# Create your views here.
from rest_framework import viewsets

from guests.models import Guest
from guests.serializers import GuestSerializer


class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
