from django.db import models


class VideoCharge(models.Model):
    video_size_mb = models.IntegerField()
    video_length = models.IntegerField()
    video_type = models.CharField(max_length=5)
