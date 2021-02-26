"""Module for sending marketing and download e-mails."""
from django.conf import settings
from django.core import serializers

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, To, Mail, ReplyTo


class BaseEmail:
    """Base abstract E-mail class."""
    from_email = Email('hello@artbootstrap.com', 'Art Bootstrap')
    reply_to = ReplyTo('eyobtariku@gmail.com', 'Eyob Tariku')
    to_email = None
    subject = None
    template_id = None

    def __init__(self):
        self.sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

    def _get_from_email(self):
        return self.from_email

    def _get_reply_to(self):
        return self.reply_to

    def _get_to_email(self):
        return self.to_email

    def _get_subject(self):
        return self.subject

    def _get_mail(self):
        from_email = self._get_from_email()
        to_email = self._get_to_email()
        subject = self._get_subject()
        reply_to = self._get_reply_to()
        mail = Mail(from_email, to_email, subject)
        mail.dynamic_template_data = self.get_dynamic_template_data()
        mail.template_id = self.template_id
        mail.reply_to = reply_to
        return mail

    def get_dynamic_template_data(self, **kwargs):
        kwargs['subject'] = self._get_subject()
        return kwargs

    def send(self):
        try:
            return self.sg.send(self._get_mail())
        except Exception as e:
            print(f'Error: {e}')
