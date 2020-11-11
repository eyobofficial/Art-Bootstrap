from django.contrib import admin

from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('first_name', 'last_name')
    filter_horizontal = ('themes', )
