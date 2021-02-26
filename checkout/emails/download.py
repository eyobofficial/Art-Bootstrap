from sendgrid.helpers.mail import To

from shared.email import BaseEmail


class PremiumDownloadEmail(BaseEmail):
    template_id = 'd-979793229b6a435599e36e0a726f4a07'

    def __init__(self, order):
        super().__init__()
        self.order = order

    def _get_to_email(self):
        full_name = f'{self.order.first_name} {self.order.last_name}'
        return To(email=self.order.email, name=full_name)

    def get_dynamic_template_data(self, **kwargs):
        kwargs.update(first_name=self.order.first_name)
        return super().get_dynamic_template_data(**kwargs)

    def send(self):
        mail = self._get_mail()
        for theme in self.order.themes.all():
            dynamic_template_data = self.get_dynamic_template_data()
            dynamic_template_data.update({
                'subject': f'{theme.title} - {theme.subtitle}',
                'theme_seo_title': theme.seo_title,
                'download_url': theme.file.url
            })
            try:
                mail.subject = f'{theme.title} - {theme.subtitle}'
                mail.dynamic_template_data = dynamic_template_data
                self.sg.send(mail)
            except Exception as e:
                print(f'Error: {e}')


class FreeDownloadEmail(BaseEmail):
    """Send e-mail link with free theme."""
    template_id = 'd-3d0bea6f2f484b3281ded502ae2d36e3'

    def __init__(self, first_name, last_name, email, theme):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.theme = theme

    def _get_to_email(self):
        full_name = f'{self.first_name} {self.last_name}'
        return To(email=self.email, name=full_name)

    def _get_subject(self):
        return self.theme.seo_title

    def get_dynamic_template_data(self, **kwargs):
        kwargs.update({
            'first_name': self.first_name,
            'theme_title': self.theme.title,
            'theme_seo_title': self.theme.seo_title,
            'download_url': self.theme.file.url,
        })
        return super().get_dynamic_template_data(**kwargs)
