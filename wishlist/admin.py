from django.contrib import admin

from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'count', 'created_at')
    filter_horizontal = ('themes', )

    def count(self, obj):
        """Returns theme count in the cart."""
        return obj.themes.count()
