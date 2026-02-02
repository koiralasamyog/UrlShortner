# mainapp/admin.py
from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'time_date_created')
    search_fields = ('original_url', 'short_url')
