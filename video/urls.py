from django.conf.urls import url, include
from rest_framework import routers

from video import views

router = routers.DefaultRouter(views.VideoViewSet)
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
