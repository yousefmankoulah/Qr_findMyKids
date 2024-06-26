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
    search_fields = ['product', 'cart']
    ordering = ['product']
    list_filter = ['product']
    list_display = ['product']
admin.site.register(CartItem, CartItemAdmin)