from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ContactFormView, MessageSentView


app_name = 'contact'

urlpatterns = [
    path(
        '',
        cache_page(60 * 60)(ContactFormView.as_view()),
        name='contact-form'
    ),
    path(
        'sent/',
        cache_page(60 * 60)(MessageSentView.as_view()),
        name='message-sent'
    ),
]
