from rest_framework import serializers

from guests.models import Guest, GuestPreferences


class GuestPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestPreferences
        fields = ('special_diet',
                  'invitation',
                  'accommodation',
                  'transport',
                  'second_day',)


class GuestSerializer(serializers.ModelSerializer):
    guest_preferences = GuestPreferencesSerializer()

    class Meta:
        model = Guest
        fields = '__all__'
        # fields = ('exp_date', 'start_date', 'title', 'premium', 'category')
