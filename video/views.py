from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import  ReadOnlyModelViewSet

from video.models import Video
from video.serializers import VideoSerializer


class VideoViewSet(ReadOnlyModelViewSet):
    queryset = Video.objects.all().order_by('-publish_date')
    permission_classes = (permissions.AllowAny, )
    serializer_class = VideoSerializer
