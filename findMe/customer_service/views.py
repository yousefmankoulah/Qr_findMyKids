from django.shortcuts import render,redirect
from .models import Customer_service
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def contactus(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_email = request.POST['customer_email']
        category = request.POST['category']
        customer_title = request.POST['customer_title']
        order_number = request.POST['order_number']
        customer_description = request.POST.get('customer_description')
        Customer_service.objects.create(customer_name=customer_name, customer_phone=customer_phone, customer_email=customer_email, category=category, customer_title=customer_title, order_number=order_number, customer_description=customer_description)
        messages.success(request, 'Thank you for your request. We will get in touch with you shortly.')
        html_message = render_to_string('customer_confirm.html', {})
        plain_message = strip_tags(html_message)
        send_mail(
            ("We recieved your request"),
            plain_message,
            "yousef.mankola10@gmail.com",
            [customer_email,],
            fail_silently=False,
            html_message=html_message
        )
        send_mail(
            ("We have a new request"),
            plain_message,
            customer_email,
            ["yousef.mankola10@gmail.com",],
            fail_silently=False,
            html_message=html_message
        )
        return redirect('category')
        
    return render(request, 'contactus.html')
