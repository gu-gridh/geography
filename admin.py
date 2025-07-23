from django.contrib.gis.db import models
from .models import *
from django.utils.html import format_html
from django.contrib.gis import admin
from diana.utils import get_fields, DEFAULT_EXCLUDE, DEFAULT_FIELDS

@admin.register(Country)
class CountryAdmin(admin.GISModelAdmin):
    fields = get_fields(Country, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display = ['name', 'code']
    list_filter = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Province)
class PlaceAdmin(admin.GISModelAdmin):
    fields = get_fields(Province, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']
    # autocomplete_fields = ['name', 'country']

@admin.register(LocalAdministrativeUnit)
class LocalAdministrativeUnitAdmin(admin.GISModelAdmin):
    fields = get_fields(LocalAdministrativeUnit, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display =  ['name', 'code', 'superregion', 'get_nuts2', 'get_nuts1', 'get_country']
    list_filter = ['name', 'superregion', 'superregion__superregion', 'superregion__superregion__superregion', 'superregion__superregion__superregion__superregion']
    search_fields = ['name', ]

    @admin.display(
        ordering='superregion__superregion__superregion__superregion',
        description='Country'
    )
    def get_country(self, obj):
        sr1 = obj.superregion
        if not sr1:
            return None

        sr2 = sr1.superregion
        if not sr2:
            return None

        sr3 = sr2.superregion
        if not sr3:
            return None

        return sr3.superregion

    @admin.display(ordering='superregion__superregion__superregion', description='NUTS1')
    def get_nuts1(self, obj):
        # Walk up three levels, but bail out early if any link is missing
        sr = obj.superregion
        if not sr:
            return None

        sr2 = sr.superregion
        if not sr2:
            return None

        return sr2.superregion

    @admin.display(ordering='superregion__superregion', description='NUTS2')
    def get_nuts2(self, obj):
        # only traverse if superregion is not None
        sr = obj.superregion
        return sr.superregion if sr and sr.superregion else None

@admin.register(NUTS3)
class NUTS3Admin(admin.GISModelAdmin):
    fields = get_fields(NUTS3, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display =   ['name', 'code','superregion', 'get_nuts1', 'get_country']
    list_filter = ['name', 'superregion', 'superregion__superregion', 'superregion__superregion__superregion']
    search_fields = ['name', ]

    @admin.display(ordering='superregion__superregion__superregion', description='Country')
    def get_country(self, obj):
        return obj.superregion.superregion.superregion

    @admin.display(ordering='superregion__superregion', description='NUTS1')
    def get_nuts1(self, obj):
        return obj.superregion.superregion

@admin.register(NUTS2)
class NUTS2Admin(admin.GISModelAdmin):
    fields = get_fields(NUTS2, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display = ['name', 'code','superregion', 'get_country']
    list_filter = ['name', 'superregion', 'superregion__superregion']
    search_fields = ['name', ]

    @admin.display(ordering='superregion__superregion__superregion', description='Country')
    def get_country(self, obj):
        return obj.superregion.superregion


@admin.register(NUTS1)
class NUTS1Admin(admin.GISModelAdmin):
    fields = get_fields(NUTS1, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display = ['name', 'code', 'superregion']
    list_filter = ['name', 'superregion']
    search_fields = ['name', ]


@admin.register(Parish)
class ParishAdmin(admin.GISModelAdmin):
    fields = get_fields(Parish, exclude=DEFAULT_EXCLUDE+["id"])
    readonly_fields = [*DEFAULT_FIELDS]
    list_display = ['name', 'code', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', ]
