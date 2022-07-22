from django.db import models


class RecieveVideo(models.Model):
    video_name = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
