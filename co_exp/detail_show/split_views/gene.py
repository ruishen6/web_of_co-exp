from django.shortcuts import render
from detail_show.models import genelist, descs, ontology, kegg

def gene_detail(request):
    accession = ''
    if request.method == 'POST':
        accession = request.POST['gene_ids']
    if request.method == 'GET':
        accession = request.GET['gene']

    gene_accessions = accession.split(',')

    desc = descs.objects.filter(geneaccession__in=gene_accessions)
    desc_dict = {}
    for item in desc:
        desc_dict[item.geneaccession] = item

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
    
    context = {'details':details, 'accession':accession}


    
    return render(request, 'detail_show/gene_detail.html', context)