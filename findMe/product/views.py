from django.shortcuts import render
from .models import Category, Product
from home.models import GenerateQr


# Create your views here.

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def product(request, category):
    product = Product.objects.filter(category=category)
    return render(request, 'product.html', {'product': product})


def prod_detail(request, id):
    product = Product.objects.filter(id=id)
    kids_name = GenerateQr.objects.filter(parent=request.user)
    return render(request, 'productDetail.html', {'product': product, 'kids': kids_name})
