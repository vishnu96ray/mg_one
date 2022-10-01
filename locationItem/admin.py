from django.contrib import admin

from .models import *


class LocationItemAdmin(admin.ModelAdmin):
    list_display = ('name','item_id','in_stock','price','solo_price','group_price','max_quantity','is_active','is_searchable','location_hierarchy_id')
    

admin.site.register(LocationItem, LocationItemAdmin)
