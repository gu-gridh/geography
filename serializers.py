from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_dynamic_fields import DynamicFieldsMixin
from . import models

from diana.abstract.models import get_fields

class ProvinceSerializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.Province
        fields = get_fields(models.Province)
        geo_field = 'geometry'