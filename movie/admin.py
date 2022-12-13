from django.contrib import admin
from .models import *
# Register your models here.

class AdminMovie(admin.ModelAdmin):
    list_display = ["judul", "overview", "genre", "rating", 'gambar']

admin.site.register(TableMovie, AdminMovie)

class TrendingMovie(admin.ModelAdmin):
    list_display = ["title", "overview", "adult", "languages", 'release', 'poster', 'vote']

admin.site.register(Trending_film, TrendingMovie)

class TopMovie(admin.ModelAdmin):
    list_display = ["title", "overview", "adult", "languages", 'release', 'poster', 'vote']

admin.site.register(top_film,TopMovie)

class ComingMovie(admin.ModelAdmin):
    list_display = ["title", "overview", "adult", "languages", 'release', 'poster', 'vote']

admin.site.register(coming_film,ComingMovie )