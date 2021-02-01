from django.urls import path

from .views import CheckoutView, PaymentDoneView


app_name = 'checkout'

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('payment-done/', PaymentDoneView.as_view(), name='payment-done'),
]
