from django.contrib import admin

from adverts.models import Advert, AdvertCategories


# Register your models here.

@admin.register(Advert)
class Advert(admin.ModelAdmin):
    model = Advert


admin.site.register(AdvertCategories)
