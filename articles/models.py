from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class KontenArtikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    gambar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.judul, self.deskripsi)
    
    class Meta:
        verbose_name_plural = 'Artikel'