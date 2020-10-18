from django.db.models import Q

from shared.mixins import BaseMixin


class BaseThemesMixin(BaseMixin):
    """Base view mixin for all `themes` app views."""

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('search', '')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) | Q(subtitle__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        kwargs['query'] = self.request.GET.get('search', '')
        return super().get_context_data(**kwargs)
