from django.urls import path

from .views import IndexView, CategoryThemeListView, ThemeListView, \
    ThemeDetailView


app_name = 'themes'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path(
        'category/<slug:slug>/',
        CategoryThemeListView.as_view(),
        name='category-theme-list'
    ),
    path('themes/', ThemeListView.as_view(), name='theme-list'),
    path(
        'themes/<slug:slug>/',
        ThemeDetailView.as_view(),
        name='theme-detail'
    )
]
