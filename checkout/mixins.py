from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from shared.mixins import BaseMixin
from cart.models import Cart


class BaseCheckoutMixin(BaseMixin, UserPassesTestMixin):
    """Base view mixin for all `checkout` app views."""

    def test_func(self):
        cart = self._get_cart()
        return cart.themes.count() > 0

    def handle_no_permission(self):
        return redirect('themes:home')

    def _get_cart(self):
        session_key = self.request.session.session_key
        return Cart.objects.get_or_create(session_key=session_key)[0]
