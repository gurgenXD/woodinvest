from django.contrib import admin
from services.models import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'desc')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )
