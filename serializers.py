from diana.abstract.serializers import DynamicDepthSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from diana.utils import get_fields, DEFAULT_FIELDS
from .models import *

class CountrySerializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = Country
        fields = get_fields(Country, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'


class LAUSerializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = LocalAdministrativeUnit
        fields = get_fields(LocalAdministrativeUnit, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'


class ProvinceSerializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = Province
        fields = get_fields(Province, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'


class NUTS1Serializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = NUTS1
        fields = get_fields(NUTS1, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'


class NUTS2Serializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = NUTS2
        fields = get_fields(NUTS2, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'


class NUTS3Serializer(GeoFeatureModelSerializer, DynamicDepthSerializer):

    class Meta:
        model = NUTS3
        fields = get_fields(NUTS3, exclude=DEFAULT_FIELDS)
        geo_field = 'geometry'
