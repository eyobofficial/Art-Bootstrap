from django.shortcuts import get_object_or_404
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


class ThemeListView(BaseThemesMixin, ListView):
    """List view for all themes."""
    template_name = 'themes/theme-list.html'
    model = Theme
    queryset = Theme.objects.filter(is_published=True)
    paginate_by = 15
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        kwargs.update({'sort': self.request.GET.get('sort', '')})
        return super().get_context_data(**kwargs)

    def get_ordering(self):
        sort = self.request.GET.get('sort')
        if sort == 'bestseller':
            return '-download_count'
        elif sort == 'price_asc':
            return 'price'
        elif sort == 'price_desc':
            return '-price'
        return super().get_ordering()


class CategoryThemeListView(ThemeListView):
    """Themes sorted by their category."""

    def get_queryset(self):
        category = self.get_category()
        qs = super().get_queryset()
        qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({'category': self.get_category()})
        return super().get_context_data(**kwargs)

    def get_category(self):
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        return category


class ThemeDetailView(BaseThemesMixin, DetailView):
    """Theme detail view."""
    model = Theme
    queryset = Theme.objects.filter(is_published=True)
    template_name = 'themes/theme-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object()
        context['related_themes'] = theme.tags.similar_objects()[:4]
        return context
