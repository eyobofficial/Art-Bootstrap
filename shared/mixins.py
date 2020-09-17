from django.views.generic.base import ContextMixin

from themes.models import Category


class BaseMixin(ContextMixin):
    """
    Base view mixin for all project views.
    """
    page_name = None

    def get_context_data(self, **kwargs):
        kwargs.update({
            'page_name': self.page_name,
            'category_list': Category.objects.order_by('id')
        })
        return super().get_context_data(**kwargs)
