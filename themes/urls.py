from django.urls import path

from .views import IndexView


app_name = 'themes'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]

