from django.urls import path,re_path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .split_views import coexp, network, gene, heatmap,boxplot

app_name = 'detail_show'
urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'co-expression?genes=(\w+)&cor=(\w+)$', views.co_expression, name='co-expression'),
    re_path(r'co-expression$', coexp.co_expression, name='co-expression'),
    path('co-search', views.co_search, name='co-search'),
    re_path(r'network$', network.network_json, name='network'),
    path('search', views.search, name='search'),
    re_path(r'gene$', gene.gene_detail, name='gene'),
    re_path(r'heatmap$', heatmap.heatmap_json, name='heatmap'),
    re_path(r'boxplot$', boxplot.boxplot_json, name='boxplot')
    # path('404_not_found', views.not_found, name='404_not_found')
]