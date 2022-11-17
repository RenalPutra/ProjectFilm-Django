from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kelamin(models.Model):
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}".format(self.gender)

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    telp = models.CharField(max_length=14)
    gender = models.ForeignKey(Kelamin, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} - {}".format(self.alamat, self.telp)
    