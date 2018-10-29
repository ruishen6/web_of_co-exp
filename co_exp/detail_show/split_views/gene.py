from django.shortcuts import render
from detail_show.models import genelist, descs, ontology, kegg, heatmap

def gene_detail(request):
    accession = ''
    if request.method == 'POST':
        accession = request.POST['gene_ids']
    if request.method == 'GET':
        accession = request.GET['gene']

    rep_gene_accessions = accession.split(',')
    rep_gene_accessions = list(set(rep_gene_accessions))
    rep_gene_accessions.sort()

    # # judge not found gene
    # all_kegg = kegg.objects.all()
    # all_accessions = []
    # for item in all_kegg:
    #     all_accessions.append(item.geneaccession)
    # rep_gene_accessions = accession.split(',')
    # rep_gene_accessions = list(set(rep_gene_accessions))

    # # if use sentence like bellow --> error occurred
    # # rep_gene_accessions = gene_accessions
    # # ????? TEA012168.1,TEA015139.1,TEA026434.1 or aa,bb
    # not_found_genes = []
    # for item in rep_gene_accessions:
    #     if item not in all_accessions:
    #         gene_accessions.remove(item)
    #         not_found_genes.append(item)
    # accession = ','.join(gene_accessions)
    # not_found_accession = ','.join(not_found_genes)
    # # if not accession:
    # #     return render(request, 'detail_show/404_not_found.html')

    desc = descs.objects.filter(geneaccession__in=rep_gene_accessions)
    desc_dict = {}
    gene_accessions = []
    for item in desc:
        desc_dict[item.geneaccession] = item
    # judge not found gene
        gene_accessions.append(item.geneaccession)
    gene_accessions = list(set(gene_accessions))
    not_found_genes = []
    for item in rep_gene_accessions:
        if item not in gene_accessions:
            not_found_genes.append(item)
    accession = ','.join(gene_accessions)
    not_found_accession = ','.join(not_found_genes)

    go = ontology.objects.filter(geneaccession__in=gene_accessions)
    go_dict = {}
    for item in go:
        go_numbers = []
        content = item.geneontology
        go_numbers = content.strip().split(',')
        go_dict[item.geneaccession] = go_numbers

    ko = kegg.objects.filter(geneaccession__in=gene_accessions)
    ko_dict = {}
    for item in ko:
        ko_numbers = []
        content = item.genekegg
        ko_numbers = content.strip().split(',')
        ko_dict[item.geneaccession] = ko_numbers

    details = []
    for item in gene_accessions:
        detail = {}
        detail['accession'] = item
        detail['desc'] = desc_dict[item]
        detail['go_number'] = go_dict[item]
        detail['ko_number'] = ko_dict[item]
        details.append(detail)
    
    heatmap_details = heatmap.objects.filter(geneaccession__in=gene_accessions)
    heatmap_total = {}
    heatmap_total['gene_num'] = len(gene_accessions)
    runs = []
    tissues = []
    tissues_num = []
    for item in heatmap_details:
        runs.append(item.runid)
        tissues.append(item.tissue)
        tissues_num.append(item.tissue)
    runs = list(set(runs))
    heatmap_total['run_num'] = len(runs)
    tissues_num = list(set(tissues_num))
    tissues_num.sort()
    heatmap_total['tissue_num'] = len(tissues_num)
    heatmap_total['tissues'] = []
    for item in tissues_num:
        content = item + ': ' + str(int(tissues.count(item)/len(gene_accessions)))
        heatmap_total['tissues'].append(content)
    


    context = {'details':details, 'accession':accession, 'not_found_accession':not_found_accession, 'heatmap_total':heatmap_total}

    return render(request, 'detail_show/gene_detail.html', context)