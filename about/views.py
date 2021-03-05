from django.views.generic import TemplateView

from .mixins import AboutMixin


class AboutUsView(AboutMixin, TemplateView):
    template_name = 'about/about-us.html'
