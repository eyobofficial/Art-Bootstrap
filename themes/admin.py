from django.contrib import admin

from .models import Category, Technology, Theme, ThemeFeature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


class ThemeFeatureInline(admin.StackedInline):
    model = ThemeFeature
    extra = 1


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'theme_version', 'download_count', 'is_featured',
        'is_published', 'is_free'
    )
    list_editable = ('is_featured', 'is_published', 'is_free', 'download_count')
    list_filter = ('category', 'is_published', 'is_featured', 'is_free')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    filter_horizontal = ('technologies', )
    inlines = [ThemeFeatureInline]
