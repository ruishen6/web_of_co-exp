# from django.http import HttpResponse, Http404
from django.shortcuts import render

def blast_analyse(request):
    # return HttpResponse('a')
    # raise Http404
    return render(request, 'detail_show/blastAnalyse.html')