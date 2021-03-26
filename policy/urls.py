from django.urls import path
from django.views.decorators.cache import cache_page

from .views import TermsAgreementView


app_name = 'policy'

urlpatterns = [
    path(
        'terms-and-agreement/',
        cache_page(60 * 60)(TermsAgreementView.as_view()),
        name='terms'
    ),
]
