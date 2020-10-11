from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, DeleteView

from shared.utils import get_session_key
from themes.models import Theme

from .mixins import BaseCartMixin
from .models import Cart


def cart_add(request, theme_slug):
    """Add items to a shopping cart."""
    theme = get_object_or_404(Theme, slug=theme_slug)
    session_key = get_session_key(request)
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    cart.themes.add(theme)
    return JsonResponse({'cart_count': cart.themes.count()})


def cart_delete(request, theme_slug):
    """Remove cart item from shopping cart."""
    session_key = get_session_key(request)
    theme = get_object_or_404(Theme, slug=theme_slug)
    cart = get_object_or_404(Cart, session_key=session_key)
    cart.themes.remove(theme)
    return redirect('cart:cart-items')


def cart_clear(request):
    """Remove all cart items from shopping cart."""
    session_key = get_session_key(request)
    cart = get_object_or_404(Cart, session_key=session_key)
    cart.themes.clear()
    return redirect('cart:cart-items')


class CartDetailView(BaseCartMixin, DetailView):
    model = Cart
    template_name = 'cart/cart-detail.html'

    def get_object(self):
        session_key = self.request.session.session_key
        return Cart.objects.get(session_key=session_key)


class CartToastView(DetailView):
    model = Theme
    template_name = 'cart/cart-toast.html'
