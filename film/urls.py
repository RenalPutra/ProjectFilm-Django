
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name='main'),
    path("trending/", trending, name='trending'),
    path("trending-sinkron/", sinkron_trending, name='sinkron_trending'),
    path("top-sinkron/", sinkron_top, name='sinkron_top'),
    path("coming-sinkron/", sinkron_coming, name='sinkron_coming'),
    path("detail_trending/<int:id>", detail_trending, name='detail_trending'),
    path("top/", top, name='top'),
    path("detail_top/<int:id>", detail_top, name='detail_top'),
    path("coming/", coming, name='coming'),
    path("detail_coming/<int:id>", detail_coming, name='detail_coming'),
    path("searchMovie/", searchMovie, name='search'),
    path("detail_movie/<int:id>", detail_search, name='detail_search'),
    path("watchlist/", watchlist_view, name='watchlist'),
    path("delete_watchlist/<int:id>", deleteWatch, name='delete_watchlist'),
    path("watchlist_trending/<int:id>", addWatchlist_trending, name='watchlist_tren'),
    path("watchlist_top/<int:id>", addWatchlist_top, name='watchlist_top'),
    path("watchlist_coming/<int:id>", addWatchlist_coming, name='watchlist_com'),
    path("watchlist_search/<int:id>", addWatchlist_search, name='watchlist_search'),
    path("about/", about, name='about'),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    # apps urls
    path("movie/", include("movie.urls")),
    path("artikels/", include("articles.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)