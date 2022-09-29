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
