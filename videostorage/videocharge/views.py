from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from videocharge.serializers import VideoChargeSerializer
from videocharge.models import VideoCharge


class VideoChargeView(ModelViewSet):
    queryset = VideoCharge.objects.all()
    serializer_class = VideoChargeSerializer
