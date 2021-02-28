from django.conf import settings
from django.views.generic.base import ContextMixin

from cart.models import Cart
from checkout.models import Order
from wishlist.models import Wishlist
from themes.models import Category, Theme

from .utils import get_session_key


class BaseMixin(ContextMixin):
    """
    Base view mixin for all project views.
    """

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.session_key = get_session_key(request)

    def get_context_data(self, **kwargs):
        cart, _ = Cart.objects.get_or_create(session_key=self.session_key)
        wishlist, _ = Wishlist.objects.get_or_create(session_key=self.session_key)
        kwargs.update({
            'category_list': Category.objects.order_by('id'),
            'featured_category_list': Category.objects.filter(
                is_featured=True).order_by('id'),
            'cart': cart,
            'wishlist': wishlist,
            'theme_count': Theme.objects.filter(is_published=True).count(),
            'sale_count': Order.objects.filter(status=Order.COMPLETED).count(),
            'facebook': settings.FACEBOOK_URL,
            'twitter': settings.TWITTER_URL,
            'instagram': settings.INSTAGRAM_URL,
            'pinterest': settings.PINTEREST_URL,
        })
        return super().get_context_data(**kwargs)
