from celery import shared_task
from celery.utils.log import get_task_logger

from .spider import get_videos
from .models import Video

logger = get_task_logger(__name__)

@shared_task
def task_get_videos():
    for video_info in get_videos():
        Video.objects.get_or_create(url=video_info['url'],
                                    name=video_info['name'])

