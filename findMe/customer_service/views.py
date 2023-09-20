from django.shortcuts import render
from .models import Customer_service

# Create your views here.

def contactus(request):
    return render(request, 'contactus.html')
