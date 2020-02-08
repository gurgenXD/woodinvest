from django.contrib import admin
from products.models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'price', 'short_desc', 'desc', 'features', 'options', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'price', 'is_active', 'created', 'updated')
    list_editable = ('is_active', 'price',)
    list_filter = ('is_active', 'category')
    search_fields = ('title', 'category', 'short_desc', 'desc', 'features', 'options')
    inlines = (ImageInline,)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )
