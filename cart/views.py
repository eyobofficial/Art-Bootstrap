from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from themes.models import Theme
from .mixins import BaseCartMixin
from .models import Cart


def cart_add(request, theme_slug):
    """Add items to a shopping cart."""
    theme = get_object_or_404(Theme, slug=theme_slug)
    if request.session.session_key is None:
        request.session.save()
    session_key = request.session.session_key
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    cart.themes.add(theme)
    return JsonResponse({'cart_count': cart.themes.count()})


class CartDetailView(BaseCartMixin, DetailView):
    model = Cart
    template_name = 'cart/cart-detail.html'

    def get_object(self):
        session_key = self.request.session.session_key
        return Cart.objects.get(session_key=session_key)


class CartToastView(DetailView):
    model = Theme
    template_name = 'cart/cart-toast.html'
