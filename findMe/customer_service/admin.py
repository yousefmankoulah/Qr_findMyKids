from django.contrib import admin
from .models import Customer_service
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class Customer_serviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['customer_name', 'customer_service_rep', 'customer_email', 'customer_phone', 'customer_title', 'order_number', 'category']
    ordering = ['ticket_date']
    list_filter = ['ticket_status', 'customer_service_rep', 'category']
    list_display = ['customer_name', 'customer_service_rep', 'order_number', 'category']
admin.site.register(Customer_service, Customer_serviceAdmin)