from django.shortcuts import render
from django.db.models import Q
from .models import Category, Product


# Create your views here.

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def product(request, category):
    product = Product.objects.filter(category=category)
    return render(request, 'product.html', {'product': product})


def prod_detail(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'productDetail.html', {'product': product})


## search

def searchResult(request):
    posts = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        posts = Product.objects.all().filter(Q(name__contains=query) |
                                            Q(description__contains=query) |
                                            Q(price__contains=query))

    return render(request, 'search.html', {'query': query, 'posts': posts})
