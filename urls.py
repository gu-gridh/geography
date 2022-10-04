from django.urls import path, include
from rest_framework import routers
from . import views
import diana.utils as utils

router = routers.DefaultRouter()
router.register(r'api/country', views.CountryViewSet, basename='country')
router.register(r'api/province', views.ProvinceViewSet, basename='province')
router.register(r'api/lau', views.LAUViewSet, basename='lau')
router.register(r'api/nuts1', views.NUTS1ViewSet, basename='nuts1')
router.register(r'api/nuts2', views.NUTS2ViewSet, basename='nuts2')
router.register(r'api/nuts3', views.NUTS3ViewSet, basename='nuts3')



urlpatterns = [
    path('', include(router.urls)),

    # Automatically generated views
    *utils.get_model_urls('geography', 'api', exclude=['province', 'country', 'lau', 'nuts1', 'nuts2', 'nuts3']),
]