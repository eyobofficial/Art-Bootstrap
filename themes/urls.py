from django.urls import path

from .views import IndexView, CategoryThemeListView, ThemeListView, \
    ThemeDetailView, FreeDownloadView


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
    ),
    path(
        'themes/<slug:slug>/download/',
        FreeDownloadView.as_view(),
        name='free-download'
    )
]
