from django.contrib import admin
from .models import Cart, CartItem
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cart_id']
    ordering = ['date_added']
    list_display = ['cart_id', 'date_added']
admin.site.register(Cart, CartAdmin)


class CartItemAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['parent', 'product', 'cart', 'kids_name']
    ordering = ['parent']
    list_filter = ['parent', 'product']
    list_display = ['parent', 'product', 'cart']
admin.site.register(CartItem, CartItemAdmin)