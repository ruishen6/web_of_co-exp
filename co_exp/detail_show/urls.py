from django.urls import path
from . import views

app_name = 'detail_show'
urlpatterns = [
    # path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]