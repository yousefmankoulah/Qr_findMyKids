from django import urls
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from qrcode import *
import time
from django.contrib import messages
from .forms import SignUpForm
from .models import GenerateQr



# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request, id):
    dashboard = GenerateQr.objects.filter(id=request.user.id)
    return render(request, 'dashboard.html', {'dashboard': dashboard})


@login_required
def createQR(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']    
        summary = request.POST['summary']    

        #saving data to database
        img_name = 'qr' + str(time.time()) + '.png'
        store_data = GenerateQr(parent = request.user, name=name, address=address, phoneNumber=phone, summary=summary, qr=img_name)    
        store_data.save()
        
        #---------------------you have to edit the link after you upload the webiste-------------------------#
        data = "http://127.0.0.1:8000/siteDetail/" + str(store_data.id)
        #----------------------------------------------------------#
        
        img = make(data)
        
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        messages.success(request, "Qr code Generated.")
    
        return render(request, 'createQR.html', {'img_name': img_name})
    return render(request, 'createQR.html')


# ---------------------Start Auth-------------#

def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def signInView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in.")
                r=str(request.user.id)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def signoutView(request):
    logout(request)
    return redirect('login')

# ---------------------End Auth-------------#
