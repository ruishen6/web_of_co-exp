from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist, descs, ontology, kegg


def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')


def search(request):
    return render(request, 'detail_show/gene_search.html')


def gene_detail(request):
    accession = ''
    if request.method == 'POST':
        accession = request.POST['gene_ids']
    if request.method == 'GET':
        accession = request.GET['gene']
    desc = descs.objects.filter(geneaccession=accession)
    go = ontology.objects.filter(geneaccession=accession)
    go_numbers = []
    for item in go:
        content = item.geneontology
        go_numbers = content.strip().split(',')
    kegg_numbers = []
    ko = kegg.objects.filter(geneaccession=accession)
    for item in ko:
        content = item.genekegg
        kegg_numbers = content.strip().split(',')
    return render(request, 'detail_show/gene_detail.html', locals())