from django.contrib import admin

from .models import Category, Tag, Technology, Theme, ThemePhoto


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'theme_version', 'is_featured',
        'is_published', 'created_at', 'updated_at'
    )
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}
