from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import descs
from .models import genelist

import json

def index(request):
    return render(request,'detail_show/home.html')


def co_search(request):
    return render(request, 'detail_show/co-search.html')

def network_json(request):
    accession = request.GET['genes']
    gene_accessions = accession.split(',')
    co_cor = request.GET.get('cor')
    gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    # context = {'gene_list':gene_list}
    # print(gene_list)
    # print(locals())
    coexpress_genes = []
    add_genes = []
    for item in gene_list:
        coexpress_genes.append(item.coexpress_gene)
    # print(coexpress_genes)
    add_gene_list = genelist.objects.filter(geneaccession__in=coexpress_genes, cor__gte=co_cor)
    judge_list = []
    for item in add_gene_list:
        # print(item.coexpress_gene)
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if item.coexpress_gene in coexpress_genes and reverse_judge not in judge_list:
            add_genes.append(item)

    # rep_add_genes = add_genes
    # for item1 in rep_add_genes:
    #     for item2 in rep_add_genes:
    #         if item1.geneaccession == item2.coexpress_gene and item1.coexpress_gene == item2.geneaccession:
    #             add_genes.remove(item1)

    # print(len(add_genes))

    edges_head = '{"edges":['
    edges = []
    for item in gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    for item in add_genes:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    nodes_head = '],"nodes":['
    nodes = []
    for item in gene_list:
        content = '{"id":"' + item.coexpress_gene + '","title":"' + item.coexpress_gene + '"}'
        nodes.append(content)
    for item in gene_accessions:
        content = '{"group":"geneGroup","id":"' + item + '","label":"' + item + '","title":"' + item + '"}'
        nodes.append(content)
    end = ']}'
    network_data = edges_head + ','.join(edges) + nodes_head + ','.join(nodes) + end
    return HttpResponse(json.dumps(network_data), content_type="application/json")

    
def co_expression(request):
    accession = request.POST['co-gene_ids']
    gene_accessions = accession.split(',')
    co_cor = request.POST['cor']
    gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    return render(request, 'detail_show/co-expression.html', locals())