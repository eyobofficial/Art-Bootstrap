import uuid as uuid_lib

from django.conf import settings
from django.db import models

from themes.models import Theme


class Wishlist(models.Model):
    """Themes favorited by a user."""
    uuid = models.UUIDField(
        db_index=True,
        editable=False,
        default=uuid_lib.uuid4
    )
    session_key = models.CharField(max_length=32, unique=True)
    themes = models.ManyToManyField(Theme, blank=True, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_key
