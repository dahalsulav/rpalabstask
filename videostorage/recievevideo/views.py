from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from recievevideo.serializers import RecieveVideoSerializer
from recievevideo.models import RecieveVideo


class RecieveVideoView(ModelViewSet):
    queryset = RecieveVideo.objects.all()
    serializer_class = RecieveVideoSerializer
