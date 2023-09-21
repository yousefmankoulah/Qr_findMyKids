import django_filters
from .models import Customer_service
from django.forms import CharField

class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Customer_service
        fields = ['customer_name', 'customer_service_rep','customer_phone', 'customer_email','customer_title','customer_description','ticket_date','ticket_status', 'order_number','category'] 
