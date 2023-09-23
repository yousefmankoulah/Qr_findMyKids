from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product, ProductReview
from home.models import GenerateQr


# Create your views here.

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def product(request, category):
    product = Product.objects.filter(category=category)
    return render(request, 'product.html', {'product': product})


def prod_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        products = Product.objects.filter(id=id)
        kids_name = GenerateQr.objects.filter(parent=request.user)
        productReview = ProductReview.objects.filter(product=product)
        return render(request, 'productDetail.html', {'product': products, 'kids': kids_name, 'productReview': productReview})
    except Product.DoesNotExist:
        # Handle the case where the product with the specified ID does not exist
        return HttpResponse("Product not found", status=404)

def review(request, id):
    product = Product.objects.get(id=id)
    user = GenerateQr.objects.filter(parent=request.user).first()
    if request.method == 'POST':
        rating_str = request.POST.get('rating')
        if rating_str is not None and rating_str != '':
            rates = int(rating_str)
        else:
            rates = 5
        comment = request.POST.get('review_text')
        rating = ProductReview.objects.create(product=product, user=user, review=rates, comment=comment)
        rating.save()
        return redirect('category')
    return render(request,'reviews.html')
