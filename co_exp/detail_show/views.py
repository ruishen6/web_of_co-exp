from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')

def network_json(request):
    return render(request, 'detail_show/network.html')

    
def co_expression(request):
    accession = request.POST['co-gene_ids']
    gene_accessions = accession.split(',')
    co_cor = request.POST['cor']
    gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    context = {'gene_list':gene_list}
    return render(request, 'detail_show/co-expression.html', context)