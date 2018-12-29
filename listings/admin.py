from django.contrib import admin

from .models import Listing
from django.contrib import humanize

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_public', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_public',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25



admin.site.register(Listing, ListingAdmin)
