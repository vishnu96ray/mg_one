from django.contrib import admin

from .models import *


class LocationHierarchyAdmin(admin.ModelAdmin):
    list_display = ('name','parent_id','stock_warehouse')
    

admin.site.register(LocationHierarchy, LocationHierarchyAdmin)
