from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category, name='category'),
    path('product/<category>/', views.product, name='product'),
    path('detail/<id>/', views.prod_detail, name='detail'),

    path('search/', views.searchResult, name='search'),


]