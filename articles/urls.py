from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", halaman_article, name="artikels"),
    path("detail_artikel/<int:id>", detail_artikel, name="detail_artikel")
]
