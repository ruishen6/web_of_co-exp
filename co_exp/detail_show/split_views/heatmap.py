from django.http import HttpResponse
from detail_show.models import heatmap

import math
import json

def heatmap_json(request):
    # get data from url like 'heatmap?genes=TEA000001.1,TEA000001.2,TEA000003.1'
    accession = request.GET['genes']
    gene_accessions = accession.split(',')

    details = heatmap.objects.filter(geneaccession__in=gene_accessions)

    y_gene_head = '[{"genes":['
    genes = []
    for item in gene_accessions:
        content = '"' + item + '"'
        genes.append(content)

    x_ssr_head = '],"ssrs":['
    ssrs = []
    for item in details:
        content = '"' + item.runid + '"'
        ssrs.append(content)
    ssrs = list(set(ssrs))

    exp_head = '],"expression":['
    exps_dict = {}
    tissues_dict = {}
    for item in details:
        key = '"' + item.geneaccession + '"' + '-' + '"' + item.runid + '"'
        exps_dict[key] = item.tpm
        tissues_dict[item.runid] = item.tissue
    exps = []
    i,j = 0,0
    for gene in genes:
        i = 0
        for ssr in ssrs:
            key = gene + '-' + ssr
            tpm = float(exps_dict[key])
            if tpm == 0:
                log_tpm = 0
            else:
                log_tpm = math.log10(float(tpm))
            content = '[' + str(i) + ',' + str(j) + ',' + str(log_tpm) + ']'
            exps.append(content)
            i += 1
        j += 1

    tissue_head = '],"tissues":['
    tissues = []
    for item in ssrs:
        item = item.strip('"')
        content = '"' + tissues_dict[item] + '"'
        tissues.append(content)

    end = ']}]'

    # json text
    heatmap_data = y_gene_head + ','.join(genes) + x_ssr_head + ','.join(ssrs) + exp_head + ','.join(exps) + tissue_head +  ','.join(tissues) + end
    # network.html
    return HttpResponse(json.dumps(heatmap_data), content_type="application/json")