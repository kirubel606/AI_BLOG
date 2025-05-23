from django.db import models

# Create your models here.
class RND(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    link = models.URLField()
    images = models.ImageField(upload_to='rnd/')
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)  # e.g. 'old-dev', 'use-case', 'issues'
