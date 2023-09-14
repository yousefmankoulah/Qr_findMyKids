from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
        ('kids_name', {'fields': ['kids_name'], }),
        ('qr', {'fields': ['qr'], }),
        ('notReady', {'fields': ['ready_to_ship'], }),
        ('ship', {'fields': ['ship'], }),

    ]
    readonly_fields = ['product', 'quantity', 'price', 'qr', 'kids_name']
    can_delete = False
    max_num = 0
    template = 'admin/order/tabular.html'
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'shippingCountry']
    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created'], }),
        ('BILLING INFORMATION', {'fields': ['emailAddress', 'billingName', 'billingAddress1'], }),
        ('SHIPPING INFORMATION', {'fields': ['shippingAddress1', 'shippingCity', 'shippingCountry'], }),
    ]
    inlines = [
        OrderItemAdmin,
    ]
    def has_delete_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request):
        return False