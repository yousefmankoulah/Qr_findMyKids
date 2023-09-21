from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from home.models import GenerateQr
from django.core.mail import send_mail

# Create your views here.


def thanks(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'thanks.html', {'customer_order': customer_order})


@login_required(login_url='login')
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
    return render(request, 'order/orders_list.html', {'order_details': order_details})

@login_required(login_url='login')
def allOrderHistory(request):
    if request.user.is_superuser:
        order_details = Order.objects.all()
    else:
        return HttpResponse("<h1>You are not welcoming in this page here</h1>")
    return render(request, 'order/all_order_list.html', {'order_details': order_details})

@login_required(login_url='login')
def NotReadyOrderHistory(request):
    if request.user.is_superuser:
        order_details = Order.objects.filter(ready_to_ship= False).order_by('id').values()
    else:
        return HttpResponse("<h1>You are not welcoming in this page here</h1>")
    return render(request, 'order/ready_to_ship.html', {'order_details': order_details})


@login_required(login_url='login')
def shippedOrderHistory(request):
    if request.user.is_superuser:
        order_details = Order.objects.filter(ship= False).order_by('id').values()
    else:
        return HttpResponse("<h1>You are not welcoming in this page here</h1>")
    return render(request, 'order/shipOrder.html', {'order_details': order_details})


@login_required(login_url='login')
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        if request.method == 'POST':
            ready = request.POST.get('ready')
            ship = request.POST.get('shipped')
            
    
            order.ready_to_ship = ready == 'on'  
            order.ship = ship == 'on'
            
            order.save()
            if order.ship == True:
                send_mail(
                    "The order has been confirmed",
                    "Your order is shipped",
                    "yousef.mankola10@gmail.com",
                    [order.emailAddress,],
                    fail_silently=False,
                    )
            return redirect('allOrderHistory')
            

    return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})