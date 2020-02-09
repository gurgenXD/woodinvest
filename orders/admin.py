from django.contrib import admin
from orders.models import *


admin.site.register(Region)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('service', 'region', 'address', 'contact', 'phone', 'email')
    list_filter = ('service', 'region')
    search_fields = ('service__title', 'region__title', 'contact', 'material', 'note')
