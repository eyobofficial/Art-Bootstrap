from django.urls import path

from .views import SubscriptionCreateView


app_name = 'shared'

urlpatterns = [
    path('subscribe/', SubscriptionCreateView.as_view(), name='subscribe')
]
