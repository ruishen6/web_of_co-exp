from django.http import HttpResponse
from detail_show.models import genelist

import json



def network_json(request):
    accession = request.GET['genes']
    gene_accessions = accession.split(',')
    co_cor = request.GET.get('cor')
    rep_gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    # context = {'gene_list':gene_list}

    judge_list = []
    gene_list = []
    coexpress_genes = []
    for item in rep_gene_list:
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if reverse_judge not in judge_list:
            gene_list.append(item)
        coexpress_genes.append(item.coexpress_gene)
    add_gene_list = genelist.objects.filter(geneaccession__in=coexpress_genes, cor__gte=co_cor)

    add_genes = []
    for item in add_gene_list:
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if item.coexpress_gene in coexpress_genes and reverse_judge not in judge_list:
            add_genes.append(item)
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
        if item.coexpress_gene not in gene_accessions:
            content = '{"id":"' + item.coexpress_gene + '","title":"' + item.coexpress_gene + '"}'
            nodes.append(content)
    for item in gene_accessions:
        content = '{"group":"geneGroup","id":"' + item + '","label":"' + item + '","title":"' + item + '"}'
        nodes.append(content)
    nodes = list(set(nodes))
    end = ']}'
    network_data = edges_head + ','.join(edges) + nodes_head + ','.join(nodes) + end
    return HttpResponse(json.dumps(network_data), content_type="application/json")