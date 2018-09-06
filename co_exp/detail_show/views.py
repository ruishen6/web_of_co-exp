from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')

    
def co_expression(request):
    gene_accession = request.POST['gene_ids']
    gene_list = genelist.objects.filter(geneaccession=gene_accession)
    context = {'gene_list':gene_list}
    return render(request, 'detail_show/co-expression.html', context)