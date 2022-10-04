from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_dynamic_fields import DynamicFieldsMixin
from . import models

from diana.abstract.models import get_fields

class CountrySerializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.Country
        fields = get_fields(models.Country)
        geo_field = 'geometry'

class ProvinceSerializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.Province
        fields = get_fields(models.Province)
        geo_field = 'geometry'

class LAUSerializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.LocalAdministrativeUnit
        fields = get_fields(models.LocalAdministrativeUnit)
        geo_field = 'geometry'

class NUTS1Serializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.NUTS1
        fields = get_fields(models.NUTS1)
        geo_field = 'geometry'

class NUTS2Serializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.NUTS2
        fields = get_fields(models.NUTS2)
        geo_field = 'geometry'

class NUTS3Serializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.NUTS3
        fields = get_fields(models.NUTS3)
        geo_field = 'geometry'