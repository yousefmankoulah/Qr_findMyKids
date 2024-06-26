from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from home.models import GenerateQr
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from order.models import Order, OrderItem
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required(login_url='login')
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
    cart_item.save()
    return redirect('cart_detail')




@login_required(login_url='login')
def cart_detail(request, total=0, counter=0, cart_items=None):
    kids_name = GenerateQr.objects.filter(parent=request.user)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'We sell everything'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        kids = request.POST.getlist('kids_name')

        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency="usd",
                description=description,
                customer=customer.id
            )
            '''creating order'''
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    billingName=billingName,
                    billingAddress1=billingAddress1,
                    billingCity=billingCity,
                    billingPostcode=billingPostcode,
                    billingCountry=billingCountry,
                    shippingName=shippingName,
                    shippingAddress1=shippingAddress1,
                    shippingCity=shippingCity,
                    shippingPostcode=shippingPostcode,
                    shippingCountry=shippingCountry
                )
                order_details.save()
                
                
                arr3 = []
                for i, j in zip(cart_items, kids):
                    kids_qr_name = GenerateQr.objects.get(parent=request.user.id, name=j)

                    arr3.append((i.product.name, i.quantity, i.product.price, kids_qr_name, kids_qr_name.name, kids_qr_name.qr))
                    order_item = OrderItem.objects.create(
                        product=i.product.name,
                        quantity=i.quantity,
                        price=i.product.price,
                        order=order_details,
                        parent=kids_qr_name,
                        kids_name=kids_qr_name.name,
                        qr=kids_qr_name.qr,
                    )
                    order_item.save()   
                    messages.success(request, "We recieved your order")              
                    cart_items.delete()
             
                html_message = render_to_string('mail_template.html', {'id': order_details.id})
                plain_message = strip_tags(html_message)
                send_mail(
                    _("The order has been confirmed"),
                    plain_message,
                    "yousef.mankola10@gmail.com",
                    [email,],
                    fail_silently=False,
                    html_message=html_message
                    )
                send_mail(
                    _("You received a new order"),
                    plain_message,
                    "yousef.mankola10@gmail.com",
                    ["yousef.mankola10@gmail.com",],
                    fail_silently=False,
                    html_message=html_message
                )
                   
                return redirect('thanks', order_details.id)
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return False, e
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total, description=description, kids_name=kids_name))



@login_required(login_url='login')
def full_remove(request, cartItem_id, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.filter(id = cartItem_id, product=product.id, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')
