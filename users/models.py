from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    is_advertiser = models.BooleanField(default=False)
    is_newlyweds = models.BooleanField(default=False)


class AdvertiserUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    tax_number = models.IntegerField(blank=True)
    company_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    country = CountryField()

    def __str__(self):
        return f"{self.name} {self.surname} at {self.company_name}"


class NewlywedsUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
