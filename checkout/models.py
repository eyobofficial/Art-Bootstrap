from django.db import models

from themes.models import Theme


class Purchase(models.Model):
    """
    Theme purchases.
    """
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    themes = models.ManyToManyField(
        Theme,
        blank=True,
        related_name='purchases'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.email
