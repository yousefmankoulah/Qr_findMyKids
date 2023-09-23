from django.contrib import admin
from .models import Category, Product, ProductReview
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'description']
    ordering = ['name']
    list_filter = ['name']
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'description', 'price']
    ordering = ['name']
    list_filter = ['name', 'category']
    list_display = ['category', 'name', 'price', 'created']
admin.site.register(Product, ProductAdmin)

admin.site.register(ProductReview)



