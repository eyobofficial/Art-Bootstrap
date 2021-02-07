from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    verbose_name = 'checkout and payments'

    def ready(self):
        import checkout.signals
