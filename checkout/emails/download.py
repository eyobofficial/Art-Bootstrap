from django.core import serializers
from django.conf import settings

from sendgrid.helpers.mail import Email, To, Content, Mail

from shared.email import BaseEmail


class DownloadEmail(BaseEmail):
    template_id = 'd-979793229b6a435599e36e0a726f4a07'

    def __init__(self, order):
        super().__init__()
        self.order = order

    def _get_to_email(self):
        full_name = f'{self.order.first_name} {self.order.last_name}'
        return To(email=self.order.email, name=full_name)

    def get_dynamic_template_data(self, **kwargs):
        order = serializers.serialize('json', [self.order])
        kwargs.update(order=order)
        return super().get_dynamic_template_data(**kwargs)

    def send(self):
        mail = self._get_mail()
        for theme in self.order.themes.all():
            dynamic_template_data = self.get_dynamic_template_data()
            dynamic_template_data.update({
                'subject': f'{theme.title} - {theme.subtitle}',
                'theme_title': theme.title,
                'theme_subtitle': theme.subtitle,
                'first_name': self.order.first_name,
                'download_url': f'{settings.HOSTNAME}{theme.file.url}'
            })
            try:
                mail.subject = f'{theme.title} - {theme.subtitle}'
                mail.dynamic_template_data = dynamic_template_data
                self.sg.send(mail)
            except Exception as e:
                print(f'Error: {e}')
