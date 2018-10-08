from django.shortcuts import render
from detail_show.models import genelist, descs, ontology, kegg

def gene_detail(request):
    accession = ''
    if request.method == 'POST':
        accession = request.POST['gene_ids']
    if request.method == 'GET':
        accession = request.GET['gene']

    gene_accessions = accession.split(',')
    length = len(gene_accessions)

    desc = descs.objects.filter(geneaccession__in=gene_accessions)
    desc_dict = {}
    for i in range(length):
        desc_dict[gene_accessions[i]] = desc[i]

    go = ontology.objects.filter(geneaccession__in=gene_accessions)
    go_dict = {}
    for i in range(length):
        go_numbers = []
        content = go[i].geneontology
        go_numbers = content.strip().split(',')
        go_dict[gene_accessions[i]] = go_numbers

    ko = kegg.objects.filter(geneaccession__in=gene_accessions)
    ko_dict = {}
    for i in range(length):
        ko_numbers = []
        content = ko[i].genekegg
        ko_numbers = content.strip().split(',')
        ko_dict[gene_accessions[i]] = ko_numbers

    details = []
    for item in gene_accessions:
        detail = {}
        detail['accession'] = item
        detail['desc'] = desc_dict[item]
        detail['go_number'] = go_dict[item]
        detail['ko_number'] = ko_dict[item]
        details.append(detail)
    
    context = {'details':details}


    
    return render(request, 'detail_show/gene_detail.html', context)