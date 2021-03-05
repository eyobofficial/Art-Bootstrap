from django.urls import path

from .views import AboutUsView


app_name = 'about'

urlpatterns = [
    path('', AboutUsView.as_view(), name='about-us'),
]
