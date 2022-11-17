from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WatchlistMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    ratings = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    gambar = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.judul, self.ratings)