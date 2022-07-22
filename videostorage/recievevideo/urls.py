from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recievevideo.views import RecieveVideoView

router = DefaultRouter()
router.register('recieve', RecieveVideoView)

urlpatterns = [
    path('', include(router.urls))
]
