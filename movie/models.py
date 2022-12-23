from django.db import models

# Create your models here.
class TableMovie(models.Model):
    judul = models.CharField(max_length=200)
    overview = models.TextField()
    genre = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    gambar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = 'Movie'
 
class Trending_film(models.Model):
    idtren = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=225)
    overview = models.TextField()
    adult = models.CharField(max_length=225)
    languages = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    vote = models.CharField(max_length=200)

class top_film(models.Model):
    idtop = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=225)
    overview = models.TextField()
    adult = models.CharField(max_length=225)
    languages = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    vote = models.CharField(max_length=200)

class coming_film(models.Model):
    idcom = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=225)
    overview = models.TextField()
    adult = models.CharField(max_length=225)
    languages = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    vote = models.CharField(max_length=200)

class searching_film(models.Model):
    idsearch = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=225)
    overview = models.TextField()
    adult = models.CharField(max_length=225)
    languages = models.CharField(max_length=200)
    release = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    vote = models.CharField(max_length=200)