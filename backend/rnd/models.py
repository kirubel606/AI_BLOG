from django.db import models
from categories.models import Category

class RND(models.Model):
    TYPE_CHOICES = [
        ('research', 'Research'),
        ('development', 'Development'),
        ('case_study', 'Case Study'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='rnd_items')
    link = models.URLField()
    coverimage = models.ImageField(upload_to='rnd/', null=True, blank=True)
    logo = models.ImageField(upload_to='rnd/', null=True, blank=True)

    # Stores multiple image paths like "rnd/file1.jpg,rnd/file2.jpg"
    images = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True)
    tags = models.CharField(max_length=255, null=True)
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='research',
    )

    def get_image_list(self):
        return self.images.split(',') if self.images else []

    def __str__(self):
        return self.title
