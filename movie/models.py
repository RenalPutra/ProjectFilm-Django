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