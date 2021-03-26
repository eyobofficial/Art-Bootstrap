from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .models import Subscription
from .mixins import BaseMixin


class SubscriptionCreateView(CreateView):
    template_name = 'shared/base.html'
    model = Subscription
    fields = ['email', ]
    success_url = reverse_lazy('themes:home')


class NotFoundView(BaseMixin, TemplateView):
    """Custom `404 Not Found` page."""
    template_name = 'shared/404.html'
