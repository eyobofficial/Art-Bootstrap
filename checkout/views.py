from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from cart.models import Cart
from .forms import CheckoutForm
from .mixins import BaseCheckoutMixin
from .models import Purchase


class CheckoutView(BaseCheckoutMixin, UserPassesTestMixin, CreateView):
    """Purchase themes in the cart."""
    model = Purchase
    form_class = CheckoutForm
    template_name = 'checkout/checkout.html'

    def test_func(self):
        session_key = self.request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key)
        return cart.themes.count() > 0

    def handle_no_permission(self):
        return redirect('themes:home')
