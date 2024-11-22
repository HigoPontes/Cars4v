from django.contrib import admin
from aplicativo.models import Cars

# Register your models here.

class CarsFilter(admin.ModelAdmin):
    list_display = ("id","user","model","brand","year")
    list_display_links = ("id","model","brand","year")
    list_filter = ("model","year")
    search_fields = ("brand","model","year")
    

admin.site.register(Cars, CarsFilter)