from django.contrib import admin
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'realtor', 'is_published', 'is_best_deal','price')
    list_display_links = ('title', 'city', 'realtor','price')
    list_editable = ('is_published', 'is_best_deal')
    list_filter = ('is_published','city', 'is_best_deal')
    search_fields = ('title','realtor','price','bedrooms','bathrooms')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)