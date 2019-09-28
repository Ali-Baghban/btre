from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'phone')
    list_display_links = ('name','email','phone',)
    list_editable = ('is_mvp',)
    list_per_page = 25
    list_filter = ('is_mvp',)
    search_fields = ('name','email','phone')
admin.site.register(Realtor, RealtorAdmin)