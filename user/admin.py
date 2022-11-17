from django.contrib import admin
from .models import *

# Register your models here.

class AdminBiodata(admin.ModelAdmin):
    list_display = ['user', 'alamat', 'telp', 'gender']

admin.site.register(Biodata)
admin.site.register(Kelamin)
