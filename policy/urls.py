from django.urls import path

from .views import TermsAgreementView


app_name = 'policy'

urlpatterns = [
    path('terms-and-agreement/', TermsAgreementView.as_view(), name='terms'),
]
