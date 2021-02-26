from django.contrib import admin

from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name',
        'is_subscribed', 'created_at'
    )
    list_filter = ('is_subscribed', 'created_at')
    list_editable = ('is_subscribed', )
    search_fields = ('email', )
