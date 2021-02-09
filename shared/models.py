from django.db import models


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        qs  = Subscription.objects.filter(email=self.email)
        if qs.exists():
            return qs.first()
        return super().save(*args, **kwargs)
