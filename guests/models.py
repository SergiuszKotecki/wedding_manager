from django.db import models

from django_countries.fields import CountryField

from users.models import NewlywedsUser


class Guest(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    owner = models.ForeignKey(NewlywedsUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.CharField(max_length=100, blank=True)
    bride_guest = models.BooleanField(default=False)
    groom_guest = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    country = CountryField()


class GuestPreferences(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, primary_key=True, related_name='guest_preferences')
    special_diet = models.BooleanField(default=False)
    invitation = models.BooleanField(default=False)
    accommodation = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    second_day = models.BooleanField(default=False)
