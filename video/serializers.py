from rest_framework import routers, serializers, viewsets
from video import models


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
