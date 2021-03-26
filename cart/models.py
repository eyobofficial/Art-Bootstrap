import uuid as uuid_lib
from functools import reduce
from operator import add

from django.conf import settings
from django.db import models

from themes.models import Theme


class Cart(models.Model):
    """
    User shopping cart.
    """
    themes = models.ManyToManyField(
        Theme,
        blank=True,
        related_name='carts'
    )
    session_key = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'

    def __str__(self):
        return self.session_key


    def get_total_amount(self):
        """Returns the total amount of the cart."""
        total = reduce(
            lambda total, item: total + item.price,
            self.themes.all(),
            0
        )
        return round(total, 2)
