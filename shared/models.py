from django.db import models


class Subscription(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField('subscribed', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        qs  = Subscription.objects.filter(email=self.email)
        if qs.exists():
            # Re-subscribe the user
            return qs.first()
        return super().save(*args, **kwargs)
