import os

from django.db import models

from users.models import CustomUser, AdvertiserUser


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class AdvertCategories(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name


class Advert(models.Model):
    CATEGORIES = (
        ('1', 'Photography'),
        ('2', 'Tailors'),
        ('3', 'Wedding articles'),
    )
    owner = models.ForeignKey(AdvertiserUser, on_delete=models.CASCADE)
    exp_date = models.DateTimeField(verbose_name='expiration_date')
    start_date = models.DateTimeField(verbose_name='start_date')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    premium = models.BooleanField(default=False)
    category = models.ManyToManyField(AdvertCategories)

    def __str__(self):
        return f"{self.owner.company_name} at {self.category.name} is {self.premium}"


class AdvertRating(models.Model):
    SCORING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    score = models.SmallIntegerField(choices=SCORING)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    advert = models.ForeignKey(Advert, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.advert.title} score: {self.score} at {self.pub_date}"
