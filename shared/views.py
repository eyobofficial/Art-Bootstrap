from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Subscription


class SubscriptionCreateView(CreateView):
    template_name = 'shared/base.html'
    model = Subscription
    fields = ['email', ]
    success_url = reverse_lazy('themes:home')
