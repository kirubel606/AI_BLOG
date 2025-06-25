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

    title = models.CharField(max_length=255,null=True,blank=True)
    title_am = models.CharField(max_length=300,null=True,blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    description_am = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    venue = models.CharField(max_length=255,null=True,blank=True)
    venue_am = models.CharField(max_length=500,null=True,blank=True)
    video_link = models.URLField(blank=True, null=True)
    # Remove single image field
    # image = models.ImageField(upload_to='events/')
    is_live = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='conference')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return self.title

# New model for multiple images
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return f"Image for {self.event.title}"
