from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from themes.models import Category, Theme


class StaticSitemap(Sitemap):
    """An XML sitemap for the static views."""
    changefreq = 'monthly'
    priority = 0.3

    def items(self):
        return ['about:about-us', 'contact:contact-form', 'policy:terms']

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    """An XML sitemap for `Category` model."""
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()

    def lastmod(self, item):
        return item.updated_at


class ThemeSitemap(Sitemap):
    """An XML sitemap for `Themes` model."""
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Theme.objects.filter(is_published=True)

    def lastmod(self, item):
        return item.updated_at
