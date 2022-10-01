from django.contrib import admin

from .models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent_id')
    

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','parent_id',)
    

class ProductProductAdmin(admin.ModelAdmin):
    list_display = ('name','categ_id','brand_id')
   
   
admin.site.register(ProductProduct, ProductProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
