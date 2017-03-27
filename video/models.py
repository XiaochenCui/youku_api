from django.db import models


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200, unique=True)
    publish_date = models.DateField('date published', auto_now_add=True)
    url = models.CharField(max_length=200, unique=True)
