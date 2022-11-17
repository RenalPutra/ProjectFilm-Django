from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, user_passes_test
from articles.models import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.


def is_operator(user):
    if user.groups.filter(name="Operator").exists():
        return True
    else:
        return False

def dashboard(request):
    template_name = "back/dashboard.html"
    if request.user.groups.filter(name="Operator").exists():
        request.session['is_operator'] = 'operator'
    
    return render(request, template_name)

@login_required
def movieTable(request):
    template_name = 'back/movie.html'
    movieCard = TableMovie.objects.all()
    context ={
        "movie" : movieCard
    }
    return render(request,template_name,context)

@login_required
def addMovie(request):
    template_name = "back/add_movie.html"
    
    if request.method == "POST" :
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        input_judul = request.POST.get("judul")
        input_overview = request.POST.get("overview")
        input_genre = request.POST.get("genre")
        input_rating = request.POST.get("rating")
        input_gambar = url
        TableMovie.objects.create(
            judul = input_judul,
            overview = input_overview,
            genre = input_genre,
            rating = input_rating,
            gambar = input_gambar
            
        )
        return redirect(movieTable)
    
        
        
        
    return render(request, template_name)

@login_required
def updateMovie(request, id):
    template_name = "add_movie.html"
    get_movie = TableMovie.objects.get(id=id)
    
    if request.method == "POST":
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        input_judul = request.POST.get("judul")
        input_overview = request.POST.get("overview")
        input_genre = request.POST.get("genre")
        input_rating = request.POST.get("rating")
        input_gambar = url
        
        get_movie.judul = input_judul
        get_movie.overview = input_overview
        get_movie.genre = input_genre
        get_movie.rating = input_rating
        get_movie.gambar = input_gambar
        get_movie.save()
        
        
        return redirect(movieTable)
    
    context ={
        "movie" : get_movie
    }
        
        
        
    return render(request, template_name, context)

@login_required
def deleteMovie(request, id):
    TableMovie.objects.get(id=id).delete()
    return redirect(movieTable)

@login_required
def table_Artikel(request):
    template_name = "back/back_artikel.html"
    
    view_all_artikel = KontenArtikel.objects.filter(nama=request.user)
    
    context ={
        "artics" : view_all_artikel
    }
    
    return render (request, template_name, context )

@login_required
def add_Artikel(request):
    template_name = "back/add_article.html"
    
    if request.method == "POST" :
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        input_judul = request.POST.get("judul")
        input_overview = request.POST.get("deskripsi")
        input_gambar = url
        penulis = request.user
        KontenArtikel.objects.create(
            nama= penulis,
            judul = input_judul,
            deskripsi = input_overview,
            gambar = input_gambar
            
        )
        return redirect(table_Artikel)
    
   
    
    return render (request, template_name)

@login_required
def edit_Artikel(request, id):
    template_name = "back/add_article.html"
    
    get_artikel = KontenArtikel.objects.get(id=id)
    
    if request.method == "POST" :
        myfile = request.FILES.get("myfile")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        input_judul = request.POST.get("judul")
        input_overview = request.POST.get("deskripsi")
        input_gambar = url
        penulis = request.user
        
        get_artikel.nama = penulis
        get_artikel.judul = input_judul
        get_artikel.deskripsi = input_overview
        get_artikel.gambar = input_gambar
        
        return redirect(table_Artikel)
    
    context = {
        "artics" : get_artikel
    }
    
    return render (request, template_name, context)

@login_required
def delete_Artikel(request, id):
    KontenArtikel.objects.get(id=id).delete()
    return redirect(table_Artikel)

@login_required
@user_passes_test(is_operator)
def users_view(request):
    template_name = "back/users_view.html"
    
    view_users = User.objects.all()
    
    context ={
        "see" : view_users
    
    }
    
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def delete_user(request, id):
    
    User.objects.get(id=id).delete()
    return redirect(users_view)

