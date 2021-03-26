"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from shared.views import NotFoundView
from .sitemaps import StaticSitemap, CategorySitemap, ThemeSitemap


# Custom `404 Not Found` view
handler404 = cache_page(60 * 60)(NotFoundView.as_view())


sitemaps = {
    'static': StaticSitemap,
    'category': CategorySitemap,
    'themes': ThemeSitemap
}

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),  # Must come before admin url
    path('admin/', admin.site.urls),

    # app urls
    path('', include('themes.urls', namespace='themes')),
    path('shared/', include('shared.urls', namespace='shared')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('contact-us/', include('contact.urls', namespace='contact')),
    path('about-us/', include('about.urls', namespace='about')),
    path('policy/', include('policy.urls', namespace='policy')),

    # Paypal URL
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Sitemap & robots
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', include('robots.urls')),
]

# Media Assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Update Admin Site Title
admin.site.site_header = admin.site.site_title = settings.PROJECT_NAME
admin.site.enable_nav_sidebar = False
