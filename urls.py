from django.urls import path, include
from rest_framework import routers
from . import views
import diana.utils as utils

router = routers.DefaultRouter()

router.register(r'api/province', views.ProvinceViewSet, basename='province')

urlpatterns = [
    path('', include(router.urls)),

    # Automatically generated views
    *utils.get_model_urls('geography', 'api', exclude=['province']),
]