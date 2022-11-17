from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from movie.models import *
from watchlist.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.hashers import make_password
from user.models import *
from django.db import transaction
import requests
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def trending(request):
    template_name = "movie/trending.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context ={
       
        "data" : data["results"]
    }
    return render(request, template_name, context)

def detail_trending(request, id):
    template_name = "movie/detail_trending.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    context ={
       
        "data" : detail,
        "data2" : hasil
    }
    return render(request, template_name, context)

def top(request):
    template_name = "movie/top.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context ={
       
        "data" : data["results"]
    }
    return render(request, template_name, context)

def detail_top(request, id):
    template_name = "movie/detail_top.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    context ={
       
        "data" : detail,
        "data2" : hasil
    }
    return render(request, template_name, context)
def coming(request):
    template_name = "movie/coming.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/upcoming?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context ={
       
        "data" : data["results"]
    }
    return render(request, template_name, context)

def detail_coming(request, id):
    template_name = "movie/detail_coming.html"
   
    
    URL = "https://api.themoviedb.org/3/movie/upcoming?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    context ={
       
        "data" : detail,
        "data2" : hasil
    }
    return render(request, template_name, context)

def searchMovie(request):
    template_name = "movie/searchMovie.html"
    global movieName
    movieName = request.POST.get("movieName")

    URL = "https://api.themoviedb.org/3/search/movie?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae&query={}".format(movieName)
    
    r = requests.get(url = URL)
    
    data = r.json()
   
    
    context ={
       
        "data" : data["results"],
        
    }
    return render(request, template_name, context)

def detail_search(request, id):
    template_name = "movie/detail_search.html"
    
    

    URL = "https://api.themoviedb.org/3/search/movie?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae&query={}".format(movieName)
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    context ={
       
        "data" : data["results"],
        "detail" : detail
    }
    return render(request, template_name, context)



def about(request):
    template_name = "about.html"
    return render(request, template_name)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(main_view)
    
    template_name = "login/login.html"
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request ,username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("username benar")
            return redirect(main_view)
        else:
            print("username salah")
        
        
    
    return render (request, template_name)

def register_view(request):
    
    template_name = "login/register.html"
    gender = Kelamin.objects.all()
    
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            alamat = request.POST.get('alamat')
            no_telp = request.POST.get('telepon')
            kelamin = request.POST.get('gender')
            
            get_gender = Kelamin.objects.get(gender=kelamin)
            
            User.objects.create(
                username = username,
                password = make_password(get_password),
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            
            get_user = User.objects.get(username=username)
            
            Biodata.objects.create(
                user = get_user,
                alamat = alamat,
                telp = no_telp,
                gender = get_gender
            )
            
            return redirect(main_view)
    
    
    context= {
        'gender' : gender
    }
    
    return render (request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect(main_view)


def main_view(request):
    
    template_name = "main.html"
    
    return render(request, template_name)

@login_required
def watchlist_view(request):
    template_name= "movie/watchlist.html"
    
    watch = WatchlistMovie.objects.filter(user=request.user)
    
    context ={
        "watch" : watch
    }
    
    return render(request, template_name, context)

@login_required
def addWatchlist_trending(request, id):
    
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    if request.method == 'POST':  
        get_judul = detail["original_title"]
        get_rate = detail["popularity"]
        get_date = detail["release_date"]
        get_gambar = detail["poster_path"]
        nama = request.user
        
        WatchlistMovie.objects.create(
            user = nama,
            judul = get_judul,
            ratings =get_rate,
            date = get_date,
            gambar = get_gambar
        )
        
        return redirect(watchlist_view)
    
    return render(request)

@login_required
def addWatchlist_top(request, id):
    
    URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    if request.method == 'POST':  
        get_judul = detail["original_title"]
        get_rate = detail["popularity"]
        get_date = detail["release_date"]
        get_gambar = detail["poster_path"]
        nama = request.user
        
        WatchlistMovie.objects.create(
            user = nama,
            judul = get_judul,
            ratings =get_rate,
            date = get_date,
            gambar = get_gambar
        )
        
        return redirect(watchlist_view)
    
    return render(request)

@login_required
def addWatchlist_coming(request, id):
    
    URL = "https://api.themoviedb.org/3/movie/upcoming?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    if request.method == 'POST':  
        get_judul = detail["original_title"]
        get_rate = detail["popularity"]
        get_date = detail["release_date"]
        get_gambar = detail["poster_path"]
        nama = request.user
        
        WatchlistMovie.objects.create(
            user = nama,
            judul = get_judul,
            ratings =get_rate,
            date = get_date,
            gambar = get_gambar
        )
        
        return redirect(watchlist_view)
    
    return render(request)

@login_required
def addWatchlist_search(request, id):
    
    URL = "https://api.themoviedb.org/3/search/movie?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae&query={}".format(movieName)
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    hasil = data['results']
    
    detail = hasil[id]
    
    if request.method == 'POST':  
        get_judul = detail["original_title"]
        get_rate = detail["popularity"]
        get_date = detail["release_date"]
        get_gambar = detail["poster_path"]
        nama = request.user
        
        WatchlistMovie.objects.create(
            user = nama,
            judul = get_judul,
            ratings =get_rate,
            date = get_date,
            gambar = get_gambar
        )
        
        return redirect(watchlist_view)
    
    return render(request)


@login_required
def deleteWatch(request, id):
    WatchlistMovie.objects.get(id=id).delete()
    
    return redirect(watchlist_view)
    
    
    