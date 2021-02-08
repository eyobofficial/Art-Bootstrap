from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from django.views.decorators.csrf import csrf_exempt

from paypal.standard.forms import PayPalPaymentsForm

from themes.models import Theme
from .forms import CheckoutForm
from .mixins import BaseCheckoutMixin
from .models import Order


class CheckoutView(BaseCheckoutMixin, CreateView):
    """Purchase themes in the cart."""
    model = Order
    form_class = CheckoutForm
    template_name = 'checkout/checkout.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'paypal_form': self._get_paypal_form(),
            'PAYPAL': Order.PAYPAL,
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        cart = self._get_cart()
        form.instance.amount = cart.get_total_amount()
        order = form.save()
        order.themes.add(*cart.themes.all())
        self.request.session['order_id'] = str(order.id)
        return JsonResponse({'order_id': order.id}, status=200)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def _get_paypal_form(self):
        cart = self._get_cart()
        host = self.request.get_host()

        # Paypal URLs
        paypal_ipn = reverse('paypal-ipn')
        paypal_done = reverse('checkout:payment-done')
        paypal_cancel = reverse('cart:cart-items')

        paypal_data = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': f'{cart.get_total_amount():2f}',
            'item_name': 'Bootstrap Template',
            'invoice': '',
            'custom': str(cart.session_key),  # Cart session key
            'currency_code': settings.PAYPAL_CURRENCY_CODE,
            'notify_url': f'http://{host}{paypal_ipn}',
            'return_url': f'http://{host}{paypal_done}',
            'cancel_return': f'http://{host}{paypal_cancel}',
        }
        return PayPalPaymentsForm(initial=paypal_data)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentDoneView(BaseCheckoutMixin, DetailView):
    model = Order
    template_name = 'checkout/download-list.html'

    def test_func(self):
        order_id = self._get_order_id()
        return order_id or Order.objects.filter(pk=order_id).exists()

    def get_object(self):
        # Get completed Order object from session
        order_id = self._get_order_id()
        return get_object_or_404(Order, pk=order_id)

    def get_context_data(self, **kwargs):
        kwargs.update(related_themes=self._get_related_themes())
        return super().get_context_data(**kwargs)

    def _get_order_id(self):
        return self.request.session.get('order_id')

    def _get_related_themes(self):
        order = self.get_object()
        order_theme_pks = [t.pk for t in order.themes.all()]
        return Theme.objects.filter(
            is_published=True
        ).exclude(pk__in=order_theme_pks).order_by('?')[:4]
