
# Register your models here.
from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'state', 'property_type')
    list_filter = ('state', 'property_type')
    search_fields = ('title', 'city') 