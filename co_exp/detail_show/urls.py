from django.urls import path,re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'detail_show'
urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'co-expression?genes=(\w+)&cor=(\w+)$', views.co_expression, name='co-expression'),
    re_path(r'co-expression$', views.co_expression, name='co-expression'),
    path('co-search', views.co_search, name='co-search'),
    re_path(r'network$', views.network_json, name='network'),
    path('search', views.search, name='search'),
    re_path(r'gene$',views.gene_detail,name='gene')
]