from django.db import models
from categories.models import Category

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
