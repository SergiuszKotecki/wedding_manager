from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by('owner')
    serializer_class = AdvertSerializer
    # permission_classes = (IsAuthenticated,)
