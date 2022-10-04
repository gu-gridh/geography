from tkinter import N
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from . import models, serializers

from diana.abstract.views import CountModelMixin, GenericPagination
from diana.abstract.models import get_fields

class ProvinceViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.Province, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination

class CountryViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.Country, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination    

class LAUViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.LocalAdministrativeUnit.objects.all()
    serializer_class = serializers.LAUSerializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.LocalAdministrativeUnit, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination

    
class NUTS1ViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.NUTS1.objects.all()
    serializer_class = serializers.NUTS1Serializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.NUTS1, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination

    
class NUTS2ViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.NUTS2.objects.all()
    serializer_class = serializers.NUTS2Serializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.NUTS2, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination

class NUTS3ViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.NUTS3.objects.all()
    serializer_class = serializers.NUTS3Serializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geometry'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = get_fields(models.NUTS3, exclude=['id', 'geometry'])

    # Specialized pagination
    pagination_class = GeoJsonPagination
