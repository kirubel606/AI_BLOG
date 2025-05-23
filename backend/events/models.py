from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='events/')
    is_live = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    