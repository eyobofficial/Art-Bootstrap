from django.views.generic import ListView, DetailView

from .mixins import BaseThemesMixin
from .models import Category, Theme


class IndexView(BaseThemesMixin, ListView):
    """Home page of theme shop."""
    model = Theme
    template_name = 'themes/index.html'
    queryset = Theme.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'featured_themes': self.get_queryset().filter(is_featured=True)
        })
        return super().get_context_data(**kwargs)
