from django import urls
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
#from qrcode import *
import time
from django.contrib import messages
from .forms import SignUpForm



# Create your views here.

def home(request):
    return render(request, 'home.html')

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
