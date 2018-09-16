from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist

import re

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')

def network_json(request):
    # accession = request.POST['co-gene_ids']
    # accession = request.GET.get('genes')
    accession = request.GET['genes']
    gene_accessions = accession.split(',')
    # co_cor = request.POST['cor']
    co_cor = request.GET.get('cor')
    gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    coexpress_genes = []
    add_genes = []
    for item in gene_list:
        coexpress_genes.append(item.coexpress_gene)
    # print(coexpress_genes)
    add_gene_list = genelist.objects.filter(geneaccession__in=coexpress_genes, cor__gte=co_cor)
    for item in add_gene_list:
        # print(item.coexpress_gene)
        if item.coexpress_gene in coexpress_genes:
            # coexpress_genes.remove(item.geneaccession)
            add_genes.append(item)
    # rep_add_genes = add_genes
    # for item1 in rep_add_genes:
    #     for item2 in rep_add_genes:
    #         if item1.geneaccession == item2.coexpress_gene and item1.coexpress_gene == item2.geneaccession:
    #             add_genes.remove(item1)

    # print(len(add_genes))
    # context = {'gene_list':gene_list}
    # print(gene_list)
    # print(locals())
    return render(request, 'detail_show/network.html', locals())

    
def co_expression(request):
    accession = request.POST['co-gene_ids']
    gene_accessions = accession.split(',')
    co_cor = request.POST['cor']
    gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    return render(request, 'detail_show/co-expression.html', locals())