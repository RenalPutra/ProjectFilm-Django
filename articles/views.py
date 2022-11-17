from django.shortcuts import render
from .models import *

# Create your views here.
def halaman_article(request):
    template_name = "artikel/articles.html"
    view_artikel = KontenArtikel.objects.all()
    
    context = {
        "artikel_view" : view_artikel
    }
    
    
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "artikel/detail_artikel.html"
    
    detail_art = KontenArtikel.objects.get(id=id)
    
    context={
        "detail" : detail_art
    }
    
    return render(request, template_name, context)