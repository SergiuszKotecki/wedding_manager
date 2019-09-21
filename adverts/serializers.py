from rest_framework import serializers

from adverts.models import Advert, AdvertCategories
from users.serializers import AdvertiserUserSerializer


class AdvertCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertCategories
        fields = ('name',)


class AdvertSerializer(serializers.ModelSerializer):
    owner = AdvertiserUserSerializer
    category = AdvertCategoriesSerializer

    class Meta:
        model = Advert
        fields = '__all__'
        # fields = ('exp_date', 'start_date', 'title', 'premium', 'category')
