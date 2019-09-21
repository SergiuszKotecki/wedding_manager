from django.db import models

# Create your models here.
from adverts.models import AdvertCategories


class TodoNote(models.Model):
    name = models.CharField(max_length=80)
    date = models.DateTimeField()
    note = models.CharField(max_length=500)
    advert_categories = models.ForeignKey(AdvertCategories, on_delete=models.CASCADE)
    priority = models.SmallIntegerField()

    class Meta:
        ordering = ('date',)
