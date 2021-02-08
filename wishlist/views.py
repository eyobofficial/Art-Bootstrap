from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

from shared.utils import get_session_key

from themes.models import Theme
from .mixins import BaseWishlistMixin
from .models import Wishlist


def favorite(request, theme_slug):
    """Add items to a user's wishlist list."""
    theme = get_object_or_404(Theme, slug=theme_slug)
    session_key = get_session_key(request)
    wishlist, _ =  Wishlist.objects.get_or_create(session_key=session_key)
    wishlist.themes.add(theme)
    return HttpResponse(status=200)


def wishlist_delete(request, theme_slug):
    """Remove favorited item from the wishlist."""
    session_key = get_session_key(request)
    theme = get_object_or_404(Theme, slug=theme_slug)
    wishlist = get_object_or_404(Wishlist, session_key=session_key)
    wishlist.themes.remove(theme)
    return redirect('wishlist:wishlist-items')


def wishlist_clear(request):
    """Remove all favorited items from the wishlist."""
    session_key = get_session_key(request)
    wishlist = get_object_or_404(Wishlist, session_key=session_key)
    wishlist.themes.clear()
    return redirect('wishlist:wishlist-items')


class WishlistDetailView(BaseWishlistMixin, DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist-detail.html'

    def get_object(self):
        return Wishlist.objects.get(session_key=self.session_key)

    def get_context_data(self, **kwargs):
        kwargs.update(related_themes=self._get_related_themes())
        return super().get_context_data(**kwargs)

    def _get_related_themes(self):
        wishlist = self.get_object()
        themes_pks = [theme.pk for theme in wishlist.themes.all()]
        return Theme.objects.filter(
            is_published=True
        ).exclude(pk__in=themes_pks).order_by('?')[:4]


class WishlistToastView(DetailView):
    model = Theme
    template_name = 'wishlist/wishlist-toast.html'
