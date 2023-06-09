# from django.contrib import admin
from django.contrib.gis import admin
from .models import Soil, SoilArea, SoilCulture, Culture
from leaflet.admin import LeafletGeoAdmin

from django.contrib import admin

from .serializers import _SoilSerializer

# Register your models here.


@admin.register(Soil)
class SoilAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "composition")
    search_fields = ("type",)


@admin.register(SoilCulture)
class SoilCultureAdmin(admin.ModelAdmin):
    list_display = ("soil", "culture")


@admin.register(SoilArea)
class SoilAreaAdmin(LeafletGeoAdmin):
    map_height = "1000px"
    map_width = "min(calc(250vw - 30px),2000px)"
    list_display = ("id", "soil", "polygon")


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_preview']
    readonly_fields = ['name', 'id', 'image']
