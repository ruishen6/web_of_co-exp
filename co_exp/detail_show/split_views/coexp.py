from django.shortcuts import render
from detail_show.models import genelist



def co_expression(request):
    accession = ''
    co_cor = ''
    if request.method == 'POST':
        accession = request.POST['co-gene_ids']
        co_cor = request.POST['cor']
    if request.method == 'GET':
        accession = request.GET['genes']
        co_cor = request.GET['cor']
    gene_accessions = accession.split(',')

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

    edges = []
    for item in gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    for item in add_genes:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    nodes = []
    for item in gene_list:
        if item.coexpress_gene not in gene_accessions:
            content = '{"id":"' + item.coexpress_gene + '","title":"' + item.coexpress_gene + '"}'
            nodes.append(content)
    for item in gene_accessions:
        content = '{"group":"geneGroup","id":"' + item + '","label":"' + item + '","title":"' + item + '"}'
        nodes.append(content)
    nodes = list(set(nodes))

    edge_number = len(edges)
    node_number = len(nodes)

    return render(request, 'detail_show/co-expression.html', locals())