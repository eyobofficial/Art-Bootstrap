from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from themes.models import Theme
from .mixins import BaseWishlistMixin
from .models import Wishlist


def favorite(request, theme_slug):
    """Add items to a user's wishlist list."""
    theme = get_object_or_404(Theme, slug=theme_slug)
    if request.session.session_key is None:
        request.session.save()
    session_key = request.session.session_key
    wishlist, _ =  Wishlist.objects.get_or_create(session_key=session_key)
    wishlist.themes.add(theme)
    return HttpResponse(status=200)


class WishlistDetailView(BaseWishlistMixin, DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist-detail.html'

    def get_object(self):
        return Wishlist.objects.get(session_key=self.session_key)


class WishlistToastView(DetailView):
    model = Theme
    template_name = 'wishlist/wishlist-toast.html'
