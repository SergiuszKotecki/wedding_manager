from rest_framework import serializers

from users.models import CustomUser, AdvertiserUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class AdvertiserUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertiserUser
        fields = ('surname',
                  'tax_number',
                  'company_name',
                  'phone_number',
                  'city',
                  'address',
                  'postal_code',
                  'country')
