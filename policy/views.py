from django.views.generic import TemplateView

from .mixins import PolicyMixin


class TermsAgreementView(PolicyMixin, TemplateView):
    """Terms and agreement view."""
    template_name = 'policy/terms-and-agreement.html'
