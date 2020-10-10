from django.urls import path

from .views import cart_add, CartDetailView, CartToastView


app_name = 'cart'


urlpatterns = [
    path('add/theme/<slug:theme_slug>/', cart_add, name='cart-add'),
    path('', CartDetailView.as_view(), name='cart-items'),
    path(
        'themes/<slug:slug>/cart-toast/',
        CartToastView.as_view(),
        name='cart-toast'
    ),
]
