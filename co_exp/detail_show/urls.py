from django.urls import path
from . import views

app_name = 'detail_show'
urlpatterns = [
    path('', views.index, name='index'),
    path('co-expression', views.co_expression, name='co-expression'),
    path('co-search/', views.co_search, name='co-search'),
    path('network', views.network_json, name='network')
]