from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_at = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    is_publication = models.BooleanField(default=False)
