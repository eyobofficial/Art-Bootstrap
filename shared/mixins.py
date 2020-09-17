from django.views.generic.base import ContextMixin

from themes.models import Category


class BaseMixin(ContextMixin):
    """
    Base view mixin for all project views.
    """
    page_title = None

    def get_context_data(self, **kwargs):
        kwargs.update({
            'page_title': self.get_page_title(),
            'category_list': Category.objects.order_by('id')
        })
        return super().get_context_data(**kwargs)

    def get_page_title(self):
        """Returns the value for `title` tag of the current page."""
        return self.page_title or ''

