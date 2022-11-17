from django.contrib import admin
from .models import *
# Register your models here.

class AdminMovie(admin.ModelAdmin):
    list_display = ["judul", "overview", "genre", "rating", 'gambar']

admin.site.register(TableMovie)