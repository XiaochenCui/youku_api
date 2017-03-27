from django.db import models


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200, unique=True)
    publish_date = models.DateField('date published')
    url = models.CharField(max_length=200, unique=True)
