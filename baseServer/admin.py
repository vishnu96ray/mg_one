from django.contrib import admin

from .models import *



class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','idd','ccd','iso_code')
    

class StateAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','country','state')
    

admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
