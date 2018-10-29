from django.shortcuts import render
from detail_show.models import genelist,kegg



def co_expression(request):
    accession = ''
    co_cor = ''
    # get form data
    if request.method == 'POST':
        accession = request.POST['co-gene_ids']
        co_cor = request.POST['cor']
    # get data from url like 'co-expression?genes=TEA000001.1&cor=0.9'
    if request.method == 'GET':
        accession = request.GET['genes']
        co_cor = request.GET['cor']
    rep_gene_accessions = accession.split(',')

    # # judge not found
    # all_kegg = kegg.objects.all()
    # all_accessions = []
    # for item in all_kegg:
    #     all_accessions.append(item.geneaccession)
    # rep_gene_accessions = accession.split(',')
    # # if use sentence like bellow --> error occurred
    # # rep_gene_accessions = gene_accessions
    # # ????? TEA012168.1,TEA015139.1,TEA026434.1
    # not_found_genes = []
    # for item in rep_gene_accessions:
    #     if item not in all_accessions:
    #         gene_accessions.remove(item)
    #         not_found_genes.append(item)
    # accession = ','.join(gene_accessions)
    # not_found_accession = ','.join(not_found_genes)

    # remove duplication from the gene_list which originated from acquired accession
    rep_gene_list = genelist.objects.filter(geneaccession__in=rep_gene_accessions, cor__gte=co_cor)
    judge_list = []
    gene_list = []
    coexpress_genes = []
    gene_accessions = []
    for item in rep_gene_list:
        judge = item.geneaccession+':'+item.coexpress_gene
        judge_list.append(judge)
        reverse_judge = item.coexpress_gene+':'+item.geneaccession
        if reverse_judge not in judge_list:
            gene_list.append(item)
        # get the coexpress_genes associated with acquired accession
        coexpress_genes.append(item.coexpress_gene)
    # judge not found
        gene_accessions.append(item.geneaccession)
    gene_accessions = list(set(gene_accessions))
    not_found_genes = []
    for item in rep_gene_accessions:
        if item not in gene_accessions:
            not_found_genes.append(item)
    accession = ','.join(gene_accessions)
    not_found_accession = ','.join(not_found_genes)

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
    edges = []
    for item in gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    for item in add_gene_list:
        content = '{"from":"' + item.geneaccession + '","title":"Value:' + item.cor + '","to":"' + item.coexpress_gene + '"}'
        edges.append(content)
    # nodes of network
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

    edge_number = len(edges)
    node_number = len(nodes)

    # locals() returns all variables within the current scope
    return render(request, 'detail_show/co-expression.html', locals())