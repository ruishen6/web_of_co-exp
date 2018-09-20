from django.http import HttpResponse
from detail_show.models import genelist

import json



def network_json(request):
    # get data from url like 'co-expression?genes=TEA000001.1&cor=0.9'
    accession = request.GET['genes']
    gene_accessions = accession.split(',')
    co_cor = request.GET.get('cor')

    # remove duplication from the gene_list which originated from acquired accession
    rep_gene_list = genelist.objects.filter(geneaccession__in=gene_accessions, cor__gte=co_cor)
    judge_list = []
    gene_list = []
    coexpress_genes = []
    for item in rep_gene_list:
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if reverse_judge not in judge_list:
            gene_list.append(item)
        # get the coexpress_genes associated with acquired accession
        coexpress_genes.append(item.coexpress_gene)

    # remove duplication from the add_gene_list which originated from the coexpress_genes
    rep_add_gene_list = genelist.objects.filter(geneaccession__in=coexpress_genes, cor__gte=co_cor)
    add_gene_list = []
    for item in rep_add_gene_list:
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if item.coexpress_gene in coexpress_genes and reverse_judge not in judge_list:
            add_gene_list.append(item)

    # edges of network
    edges_head = '{"edges":['
    edges = []
    for item in gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    for item in add_gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    # nodes of network
    nodes_head = '],"nodes":['
    nodes = []
    for item in gene_list:
        if item.coexpress_gene not in gene_accessions:
            content = '{"id":"' + item.coexpress_gene + '","title":"' + item.coexpress_gene + '"}'
            nodes.append(content)
    for item in gene_accessions:
        content = '{"group":"geneGroup","id":"' + item + '","label":"' + item + '","title":"' + item + '"}'
        nodes.append(content)
    # remove duplication from nodes
    nodes = list(set(nodes))
    end = ']}'

    # json text
    network_data = edges_head + ','.join(edges) + nodes_head + ','.join(nodes) + end
    # network.html
    return HttpResponse(json.dumps(network_data), content_type="application/json")