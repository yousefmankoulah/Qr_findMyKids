from django.contrib import admin
from .models import GenerateQr
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class QRAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'address', 'phoneNumber']
    ordering = ['name']
    list_filter = ['name', 'parent']
    list_display = ['parent', 'name', 'phoneNumber']
admin.site.register(GenerateQr, QRAdmin)