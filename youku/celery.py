import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
app = Celery('youku')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_shcedule = {
    # Executes every day at 0:0 a.m.
    'scrapy-video': {
        'task': 'task_get_videos',
        'schedule': crontab(minute='*'),
    }
}