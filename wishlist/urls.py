from django.urls import path, include

from .views import favorite, WishlistDetailView, WishlistToastView


app_name = 'wishlist'

urlpatterns = [
    path('', WishlistDetailView.as_view(), name='wishlist-items'),
    path('add/theme/<slug:theme_slug>/', favorite, name='favorite'),
    path(
        'themes/<slug:slug>/wishlist-toast/',
        WishlistToastView.as_view(),
        name='wishlist-toast'
    )
]
