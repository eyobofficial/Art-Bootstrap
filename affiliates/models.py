from django.db import models
from django.utils.translation import gettext_lazy as _


class Affiliate(models.Model):
    name = models.CharField(max_length=120,
                            help_text=_('Affiliate provider name.'))
    website = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    title = models.CharField(max_length=120,
                             help_text=_('Affiliate program title'))
    affiliate = models.ForeignKey(Affiliate, on_delete=models.PROTECT)
    summary = models.TextField(blank=True)
    service = models.URLField(max_length=255, blank=True, null=True)
    _active_help_text = _('This affiliate program is currently active.')
    active = models.BooleanField(default=False, help_text=_active_help_text)
    date_joined = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Affiliate Program')
        verbose_name_plural = _('Affiliate Programs')

    def __str__(self):
        return self.title
