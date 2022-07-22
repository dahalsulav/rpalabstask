from django.urls import path, include
from rest_framework.routers import DefaultRouter
from videocharge.views import VideoChargeView

router = DefaultRouter()
router.register('calculate', VideoChargeView)

urlpatterns = [
    path('', include(router.urls))
]
