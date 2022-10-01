from django.contrib import admin

from .models import *


class AddressAdmin(admin.ModelAdmin):
    list_display = ('mobile',)
    
admin.site.register(Address, AddressAdmin)
