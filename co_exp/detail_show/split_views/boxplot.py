from django.shortcuts import HttpResponse
from detail_show.models import heatmap

import math
import json

def boxplot_json(request):
    # get data from url like 'boxplot?gene=TEA000001.1,TEA000001.2,TEA000003.1'
    accession = request.GET['gene']
    # gene_accessions = accession.split(',')
    rep_details = heatmap.objects.filter(geneaccession=accession)

    # sort by tissue
    tissues_ready = []
    values_ready = {}
    for item in rep_details:
        tissues_ready.append(item.tissue)
    tissues_ready = list(set(tissues_ready))
    tissues_ready.sort()
    details = []
    for tissue_item in tissues_ready:
        values_ready[tissue_item] = []
        for item in rep_details:
            if tissue_item == item.tissue:
                details.append(item)

    for item in details:
            values_ready[item.tissue].append(item.tpm)
    
    # sorted_key_list = sorted(values_ready)
    # sorted_values = map(lambda x:{x:values_ready[x]}, sorted_key_list)
    # dict sorted to a list

    # json data
    values_head = '[{"values":['
    tissue_head = '],"tissues":['
    values = []
    tissues = []
    for key,value in values_ready.items():
        value_content = '[' + ','.join(value) + ']'
        values.append(value_content)
        tissue_content = '"' + key + '"'
        tissues.append(tissue_content)

    end = ']}]'

    heatmap_data = values_head + ','.join(values) + tissue_head +  ','.join(tissues) + end

    return HttpResponse(json.dumps(heatmap_data), content_type="application/json")