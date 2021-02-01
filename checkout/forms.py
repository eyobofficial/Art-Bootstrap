from django import forms

from .models import Order


class CheckoutForm(forms.ModelForm):
    """Form for creating/updating `Purchase` model instances."""

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'payment_method']

