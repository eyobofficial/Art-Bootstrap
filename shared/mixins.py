from django.views.generic.base import ContextMixin

from cart.models import Cart
from wishlist.models import Wishlist
from themes.models import Category


class BaseMixin(ContextMixin):
    """
    Base view mixin for all project views.
    """

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.session_key = self._get_session_key()

    def get_context_data(self, **kwargs):
        cart, _ = Cart.objects.get_or_create(session_key=self.session_key)
        wishlist, _ = Wishlist.objects.get_or_create(session_key=self.session_key)
        kwargs.update({
            'category_list': Category.objects.order_by('id'),
            'cart': cart,
            'wishlist': wishlist
        })
        return super().get_context_data(**kwargs)

    def _get_session_key(self):
        """Returns a session key for the current user."""
        if self.request.session.session_key is None:
            self.request.session.save()
        return self.request.session.session_key
