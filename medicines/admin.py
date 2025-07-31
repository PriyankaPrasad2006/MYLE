from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'batch_number', 'manufacturer', 'manufacturing_date', 'expiry_date', 'created_at']
    list_filter = ['manufacturer', 'manufacturing_date', 'expiry_date']
    search_fields = ['name', 'batch_number', 'manufacturer']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
