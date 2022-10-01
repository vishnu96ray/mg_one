from django.contrib import admin

from .models import *


class StockWarehouseAdmin(admin.ModelAdmin):
    list_display = ('code','name','is_active')
    

admin.site.register(StockWarehouse, StockWarehouseAdmin)
