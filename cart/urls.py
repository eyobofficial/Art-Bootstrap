from django.urls import path

from .views import cart_add, cart_delete, cart_clear, CartDetailView

app_name = 'cart'


urlpatterns = [
    path('add/themes/<slug:theme_slug>/', cart_add, name='cart-add'),
    path('clear/', cart_clear, name='cart-clear'),
    path('delete/themes/<slug:theme_slug>/', cart_delete, name='cart-delete'),
    path('', CartDetailView.as_view(), name='cart-items'),
]
