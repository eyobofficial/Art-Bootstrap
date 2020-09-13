import uuid

from django.db import models


class Category(models.Model):
    """Bootstrap theme category."""
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Theme tag."""
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Technology(models.Model):
    """Technology stacks used in the theme."""
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Theme(models.Model):
    """Bootstrap themes."""
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='themes'
    )
    tags = models.ManyToManyField(Tag, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    description = models.TextField(blank=True)
    theme_version = models.FloatField(null=True, blank=True)
    bootstrap_version = models.FloatField(null=True, blank=True)
    is_published = models.BooleanField('published', default=True)
    is_featured = models.BooleanField('featured', default=False)
    thumbnail = models.ImageField(null=True, blank=True)
    file = models.FileField(
        'theme file',
        null=True, blank=True,
        help_text='Archived theme file.'
    )
    preview_url = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class ThemePhoto(models.Model):
    """Bootstrap theme photos."""
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    photo = models.ImageField()
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Theme Photo'
        verbose_name_plural = 'Theme Photos'

    def __str__(self):
        return self.title
