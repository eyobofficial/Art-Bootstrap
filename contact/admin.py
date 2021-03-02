from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'get_sender', 'sent_at')
    list_filter = ('sent_at', )
    search_fields = ('first_name', 'last_name', 'email', 'subject', 'content')

    def get_sender(self, obj):
        """Returns the e-mail"""
        return f'{obj.first_name} {obj.last_name} <{obj.email}>'

    get_sender.short_description = 'From'
