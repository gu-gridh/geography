from django.contrib.gis.db import models
from .models import *
from django.utils.html import format_html
from django.contrib.gis import admin
from diana.utils import get_fields, DEFAULT_EXCLUDE

@admin.register(Country)
class CountryAdmin(admin.OSMGeoAdmin):
    fields = get_fields(Country, exclude=DEFAULT_EXCLUDE+["id"])
    list_display = ['name', 'code']
    list_filter = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Province)
class PlaceAdmin(admin.OSMGeoAdmin):
    fields = get_fields(Province, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = []
    list_display = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']
    # autocomplete_fields = ['name', 'country']

@admin.register(LocalAdministrativeUnit)
class LocalAdministrativeUnitAdmin(admin.OSMGeoAdmin):
    fields = get_fields(LocalAdministrativeUnit, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = []
    list_display =  ['name', 'code', 'nuts3', 'get_nuts2', 'get_nuts1', 'get_country']
    list_filter = ['name', 'nuts3', 'nuts3__nuts2', 'nuts3__nuts2__nuts1', 'nuts3__nuts2__nuts1__country']
    search_fields = ['name', ]

    @admin.display(ordering='nuts3__nuts2__nuts1__country', description='Country')
    def get_country(self, obj):
        return obj.nuts3.nuts2.nuts1.country

    @admin.display(ordering='nuts3__nuts2__nuts1', description='NUTS1')
    def get_nuts1(self, obj):
        return obj.nuts3.nuts2.nuts1

    @admin.display(ordering='nuts3__nuts2', description='NUTS2')
    def get_nuts2(self, obj):
        return obj.nuts3.nuts2

@admin.register(NUTS3)
class NUTS3Admin(admin.OSMGeoAdmin):
    fields = get_fields(NUTS3, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = []
    list_display =   ['name', 'code','nuts2', 'get_nuts1', 'get_country']
    list_filter = ['name', 'nuts2', 'nuts2__nuts1', 'nuts2__nuts1__country']
    search_fields = ['name', ]

    @admin.display(ordering='nuts2__nuts1__country', description='Country')
    def get_country(self, obj):
        return obj.nuts2.nuts1.country

    @admin.display(ordering='nuts2__nuts1', description='NUTS1')
    def get_nuts1(self, obj):
        return obj.nuts2.nuts1

@admin.register(NUTS2)
class NUTS2Admin(admin.OSMGeoAdmin):
    fields = get_fields(NUTS2, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = []
    list_display = ['name', 'code','nuts1', 'get_country']
    list_filter = ['name', 'nuts1', 'nuts1__country']
    search_fields = ['name', ]

    @admin.display(ordering='nuts2__nuts1__country', description='Country')
    def get_country(self, obj):
        return obj.nuts1.country


@admin.register(NUTS1)
class NUTS1Admin(admin.OSMGeoAdmin):
    fields = get_fields(NUTS1, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = []
    list_display = ['name', 'code', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', ]
