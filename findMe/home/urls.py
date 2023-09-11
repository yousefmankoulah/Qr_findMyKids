from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.signInView, name='login'),
    path('logout/', views.signoutView, name='logout'),
    path('register/', views.register, name="register"),

    
]