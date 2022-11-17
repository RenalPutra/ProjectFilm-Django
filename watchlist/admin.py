from django.contrib import admin
from .models import  *
# Register your models here.

class AdminWatchlist(admin.ModelAdmin):
    list_display= ["user","judul", "ratings", "date", "gambar"]

admin.site.register(WatchlistMovie)