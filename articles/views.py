from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def halaman_article(request):
    template_name = "artikel/articles.html"
    view_artikel = KontenArtikel.objects.all()
    
    p = Paginator(KontenArtikel.objects.all(), 4)
    page = request.GET.get('page')
    pager =p.get_page(page)
    nums = "a" * pager.paginator.num_pages
    
    context = {
        "artikel_view" : view_artikel,
        "pager" : pager,
        "nums" : nums
    }
    
    
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "artikel/detail_artikel.html"
    
    detail_art = KontenArtikel.objects.get(id=id)
    
    context={
        "detail" : detail_art
    }
    
    return render(request, template_name, context)