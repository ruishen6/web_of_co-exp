from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')


def search(request):
    return render(request, 'detail_show/gene_search.html')

def blast(request):
    return render(request, 'detail_show/blast.html')

def not_found(request):
    return render(request, 'detail_show/404.html')
    # return render_to_response('404.html')