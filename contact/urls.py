from django.urls import path

from .views import ContactFormView, MessageSentView


app_name = 'contact'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact-form'),
    path('sent/', MessageSentView.as_view(), name='message-sent'),
]
