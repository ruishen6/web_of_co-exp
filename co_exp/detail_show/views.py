from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')


def search(request):
    return render(request, 'detail_show/gene_search.html')

# def not_found(request):
#     return render(request, 'detail_show/404_not_found.html')