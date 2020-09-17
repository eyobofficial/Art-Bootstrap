from django.contrib import admin

from .models import Category, Tag, Technology, Theme, ThemePhoto


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


class ThemePhotoInline(admin.StackedInline):
    model = ThemePhoto
    extra = 1


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'theme_version', 'is_featured',
        'is_published', 'created_at'
    )
    list_editable = ('is_featured', 'is_published')
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ('tags', 'technologies')
    inlines = (ThemePhotoInline, )
