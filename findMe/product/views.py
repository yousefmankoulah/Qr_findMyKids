from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product, ProductReview
from home.models import GenerateQr
from order.models import OrderItem
from django.contrib.auth.decorators import login_required


# Create your views here.

def category(request):
    category = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def product(request, category):
    products = Product.objects.filter(category=category)

    product_data = []  
    for product in products:
        productReview = ProductReview.objects.filter(product=product)

        rating_sum = 0
        review_count = 0

        for review in productReview:
            rating_sum += review.review
            review_count += 1

        average_rating = rating_sum / review_count if review_count > 0 else 0
        count = productReview.count()

        # Store product data in a dictionary
        product_data.append({
            'product': product,
            'count': count,
            'average_rating': average_rating,
        })
    
    return render(request, 'product.html', {'product_data': product_data})


@login_required(login_url='login')
def prod_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        products = Product.objects.filter(id=id)
        kids_name = GenerateQr.objects.filter(parent=request.user).first()
        productReview = ProductReview.objects.filter(product=product)
        usercomment = ProductReview.objects.filter(user=kids_name, product=product)
        orderBefore = OrderItem.objects.filter(parent=kids_name, product=product)

        rating_sum = 0
        review_count = 0

        for review in productReview:
            rating_sum += review.review
            review_count += 1

        # Calculate the average rating, handling the case where there are no reviews
        average_rating = rating_sum / review_count if review_count > 0 else 0
        count = productReview.count()
     
        context = {'product': products, 
                   'kids': kids_name, 
                   'productReview': productReview, 
                   'usercomment': usercomment, 
                   'orderBefore': orderBefore,
                   'average_rating': average_rating,
                   'count': count,}

        return render(request, 'productDetail.html', context)
    except Product.DoesNotExist:
        # Handle the case where the product with the specified ID does not exist
        return HttpResponse("Product not found", status=404)


@login_required(login_url='login')
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
