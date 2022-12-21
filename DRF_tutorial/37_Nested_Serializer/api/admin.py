from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration']