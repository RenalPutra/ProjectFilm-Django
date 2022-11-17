from django.contrib import admin
from .models import *
# Register your models here.

class AdminArtikel(admin.ModelAdmin):
    list_display = ["judul", "deskripsi", "date"]

admin.site.register(KontenArtikel, AdminArtikel)