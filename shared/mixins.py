from django.views.generic.base import ContextMixin


class BaseMixin(ContextMixin):
    """
    Base view mixin for all project views.
    """
    page_name = None

    def get_context_data(self, **kwargs):
        kwargs.update(page_name=self.page_name)
        return super().get_context_data(**kwargs)
