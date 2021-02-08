from django.urls import path, include

from .views import favorite, wishlist_delete, wishlist_clear, \
    WishlistDetailView, WishlistToastView


app_name = 'wishlist'

urlpatterns = [
    path('', WishlistDetailView.as_view(), name='wishlist-items'),
    path('add/themes/<slug:theme_slug>/', favorite, name='favorite'),
    path(
        'delete/themes/<slug:theme_slug>/',
        wishlist_delete,
        name='wishlist-delete'
    ),
    path('clear/', wishlist_clear, name='wishlist-clear'),
    path(
        'themes/<slug:slug>/wishlist-toast/',
        WishlistToastView.as_view(),
        name='wishlist-toast'
    )
]
