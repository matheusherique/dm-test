   
from django.urls import path, include
from rest_framework import routers
from .views import SolicitationViewSet

router = routers.DefaultRouter()
router.register(r'list', SolicitationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]