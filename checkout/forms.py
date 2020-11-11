from django import forms

from .models import Purchase


class CheckoutForm(forms.ModelForm):
    """Form for creating/updating `Purchase` model instances."""

    class Meta:
        model = Purchase
        fields = ['first_name', 'last_name', 'email', 'themes']
