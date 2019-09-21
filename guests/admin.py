from django.contrib import admin

# Register your models here.
from django.contrib.admin.options import InlineModelAdmin

from guests.models import Guest, GuestPreferences


class GuestPreferencesInline(admin.TabularInline):
    model = GuestPreferences


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    model = Guest
    inlines = (GuestPreferencesInline,)
