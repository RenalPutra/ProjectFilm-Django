from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path("movie/", movieTable, name='movie'),
    path("table_artikel/", table_Artikel, name="viewArtikel"),
    path("table_users/", users_view, name="usersView"),
    path("delete_users/<int:id>", delete_user, name="deleteUser"),
    path("add_artikel/", add_Artikel, name="addArtikel"),
    path("edit_artikel/<int:id>", edit_Artikel, name="editArtikel"),
    path("delete_artikel/<int:id>", delete_Artikel, name="deleteArtikel"),
    path("addmovie/", addMovie, name='add'),
    path("updatemovie/<int:id>", updateMovie, name='update'),
    path("deletemovie/<int:id>", deleteMovie, name='delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 