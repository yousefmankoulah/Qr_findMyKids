from django.urls import path
from . import views



urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('full_remove/<int:cartItem_id>/<int:id>', views.full_remove, name='full_remove'),
]