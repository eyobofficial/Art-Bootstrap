from django.urls import path
from django.views.decorators.cache import cache_page

from .views import AboutUsView


app_name = 'about'

urlpatterns = [
    path('', cache_page(60 * 60)(AboutUsView.as_view()), name='about-us'),
]
