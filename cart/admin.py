from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'session_key',
        'count',
        'amount',
        'created_at'
    )
    filter_horizontal = ['themes']
    readonly_fields = ('session_key', 'created_at')

    def count(self, obj):
        """Returns theme count in the cart."""
        return obj.themes.count()

    def amount(self, obj):
        return obj.get_total_amount()
