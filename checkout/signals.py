from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from cart.models import Cart

from paypal.standard.ipn.signals import valid_ipn_received
from .emails.download import PremiumDownloadEmail
from .models import Order


@receiver(valid_ipn_received)
def paypal_payment_completed(sender, **kwargs):
    """Perform clean up tasks when Paypal payment is completed."""
    ipn = sender
    if ipn.payment_status == 'Completed':
        order = get_object_or_404(Order, pk=ipn.invoice)

        if ipn.mc_gross == order.amount:
            order.status == Order.COMPLETED
            order.save()
            cart_session_key = ipn.custom

            # E-mail download links
            PremiumDownloadEmail(order).send()
            for theme in order.themes.all():
                theme.download_count += 1
                theme.save()

            # Reset shopping cart
            try:
                cart = Cart.objects.get(session_key=cart_session_key)
                cart.themes.clear()
            except Cart.DoesNotExist:
                pass

