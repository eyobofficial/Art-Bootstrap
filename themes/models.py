import uuid as uuid_lib

from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from taggit.managers import TaggableManager


def themes_upload_location(instance, filename):
    """
    Location for uploading theme files.
    """
    return f'themes/{uuid_lib.uuid4()}/{filename}'


class Category(models.Model):
    """Bootstrap theme category."""
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(
        'SEO description',
        help_text='Category description upto 160 charchaters for SEO.',
        max_length=160
    )
    is_featured = models.BooleanField('featured', default=False)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('themes:category-theme-list', args=[self.slug])

    @cached_property
    def keywords(self):
        return ', '.join([tag.name.lower() for tag in self.tags.all()])


class Technology(models.Model):
    """Technology stacks used in the theme."""
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.title


class Theme(models.Model):
    """Bootstrap themes."""

    # Bootstrap Versions
    BOOTSTRAP_3 = 3
    BOOTSTRAP_4 = 4
    BOOTSTRAP_5 = 5

    BOOTSTRAP_VERSION_OPTIONS = (
        (BOOTSTRAP_3, '3.x'),
        (BOOTSTRAP_4, '4.x'),
        (BOOTSTRAP_5, '5.x'),
    )

    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='themes'
    )
    tags = TaggableManager()
    technologies = models.ManyToManyField(Technology, blank=True)
    description = models.TextField(blank=True)
    seo_description = models.TextField(
        'SEO description',
        max_length=160,
        blank=True,
        help_text='Description to display in the meta tag.'
    )
    theme_version = models.CharField(max_length=10, blank=True, default='')
    bootstrap_version = models.IntegerField(
        choices=BOOTSTRAP_VERSION_OPTIONS,
        default=BOOTSTRAP_4
    )
    is_published = models.BooleanField('published', default=True)
    is_featured = models.BooleanField('featured', default=False)
    photo = models.ImageField(
        null=True, blank=True,
        help_text='Recommended size 900x600 px.'
    )
    file = models.FileField(
        'theme file',
        upload_to=themes_upload_location,
        null=True, blank=True,
        help_text='Archived theme file.'
    )
    preview_url = models.URLField(
        max_length=255,
        blank=True,
        help_text='URL to deployed verion of the website.'
    )
    source_url = models.URLField(
        max_length=255,
        blank=True,
        help_text='URL to original theme website.'
    )
    repo_url = models.URLField(
        max_length=255,
        blank=True,
        help_text='URL to the repository.'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_free = models.BooleanField(
        'free',
        default=False,
        help_text='Not a premium theme.'
    )
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('themes:theme-detail', args=[self.slug])

    @cached_property
    def seo_title(self):
        return f'{self.title} — {self.subtitle}'

    @cached_property
    def keywords(self):
        return ', '.join([tag.name.lower() for tag in self.tags.all()])


class ThemeFeature(models.Model):
    """Features of the template."""
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='features'
    )
    summary = models.CharField(max_length=255)

    class Meta:
        order_with_respect_to = 'theme'

    def __str__(self):
        return self.summary
