from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist

def detail(request):
    gene_list = genelist.objects.order_by('-geneaccession')[:10]
    context = {'gene_list':gene_list,}
    return render(request, 'detail_show/detail.html', context)

def search(request):
    if request.method == 'POST':
        gene_accession = request.POST['gene_ids']
    gene_list = genelist.objects.filter(geneaccession=gene_accession)

    return HttpResponseRedirect(reversed('detail_show:detail'))
    

# def index(request):
    # return HttpResponse('hello')