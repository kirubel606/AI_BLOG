from django.db import models
from categories.models import Category
from django.utils import timezone

class Event(models.Model):
    TYPE_CHOICES = [
        ('conference', 'Conference'),
        ('webinar', 'Webinar'),
        ('workshop', 'Workshop'),
    ]

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    venue = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='events/')
    is_live = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='conference')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return self.title
