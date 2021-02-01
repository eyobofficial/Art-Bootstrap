from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'amount',
        'payment_method', 'status', 'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('themes', )
