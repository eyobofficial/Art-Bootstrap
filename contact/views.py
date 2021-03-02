from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from shared.models import Subscription
from .mixins import ContactMixin
from .models import Message


class ContactFormView(ContactMixin, CreateView):
    model = Message
    fields = ('first_name', 'last_name', 'email', 'subject', 'content')
    template_name = 'contact/contact-form.html'
    success_url = reverse_lazy('contact:message-sent')

    def form_valid(self, form):
        self._subscribe_user(form)
        return super().form_valid(form)

    @staticmethod
    def _subscribe_user(form):
        """Add user to the subscription model."""
        user_data = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email']
        }
        Subscription.objects.create(**user_data)


class MessageSentView(ContactMixin, TemplateView):
    template_name = 'contact/message-sent.html'
