import uuid as uuid_lib

from django.db import models
from django.utils.functional import cached_property

from themes.models import Theme


class Order(models.Model):
    """
    Theme purchases.
    """

    # Payment methods
    PAYPAL = 1
    STRIPE = 2

    PAYMENT_METHOD_CHOICES = (
        (PAYPAL, 'PayPal'),
        (STRIPE, 'Stripe'),
    )

    # Order status
    CHECKOUT  = 1
    PENDING   = 2
    COMPLETED = 3
    CANCELLED = 4

    ORDER_STATUS_CHOICES = (
        (CHECKOUT, 'Checkout'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    )

    id = models.UUIDField(
        primary_key=True, editable=False,
        default=uuid_lib.uuid4
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    themes = models.ManyToManyField(
        Theme,
        blank=True,
        related_name='purchases'
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )
    payment_method = models.IntegerField(
        choices=PAYMENT_METHOD_CHOICES,
        blank=True, null=True
    )
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=CHECKOUT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.pk)

    @cached_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
