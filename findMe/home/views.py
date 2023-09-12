from django import urls
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from qrcode import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm
from .models import GenerateQr




# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def dashboard(request, id):
    dashboard = GenerateQr.objects.filter(parent=request.user).order_by('-name')
    return render(request, 'dashboard.html', {'dashboard': dashboard})


@login_required(login_url='login')
def createQR(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']    
        summary = request.POST['summary']    

        #saving data to database
        img_name = 'qr_' + name + '.png'
        store_data = GenerateQr(parent = request.user, name=name, address=address, phoneNumber=phone, summary=summary, qr=img_name)    
        store_data.save()
        
        #---------------------you have to edit the link after you upload the webiste-------------------------#
        data = "https://glowing-fortnight-pwq79wrrrv3r4q5-8000.app.github.dev/profileDetail/" + str(store_data.id)
        #----------------------------------------------------------#
        
        img = make(data)
        
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        messages.success(request, "Qr code Generated.")
    
        return render(request, 'createQR.html', {'img_name': img_name})
    return render(request, 'createQR.html')



def profileDetail(request, id):
    qr = GenerateQr.objects.filter(id=id)
    return render(request, 'profileDetail.html', {'qr': qr})



@login_required(login_url='login')
def updateProfile(request, id):
    profile = GenerateQr.objects.get(id=id)

    if profile.parent == request.user:
        if request.method == 'POST':
            name = request.POST['name']
            address = request.POST['address']
            phone = request.POST['phoneNumber']
            summary = request.POST['summary']    

            profile.name = name
            profile.address = address
            profile.phoneNumber = phone
            profile.summary = summary
          
            profile.save()

            return redirect('profileDetail', id=profile.id)
    else:
        messages.error(request, "you can't edit this post")
    return render(request, 'updateProfile.html', {'profile': profile})



@login_required(login_url='login')
def delete_post(request, id):
    profile = GenerateQr.objects.get(id=id)
    if profile.parent == request.user:
        profile.delete()
    else:
        messages.error(request, "you can't delete this post")
    return redirect('dashboard', id=request.user)


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
                return redirect('dashboard', id=request.user.id)
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password/password_reset.html'
    email_template_name = 'password/password_reset_email.html'
    subject_template_name = 'password/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')
    





def signoutView(request):
    logout(request)
    return redirect('login')

# ---------------------End Auth-------------#
