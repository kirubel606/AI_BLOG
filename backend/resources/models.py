from django.db import models
from categories.models import Category

# Create your models here.
class Resource(models.Model):
    CLASSIFICATION_CHOICES = [
     ('publication', 'Publication'),
     ('case_study', 'Case Study'),
     ('development', 'Development'),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_at = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=255)
    classification = models.CharField(max_length=20,choices=CLASSIFICATION_CHOICES,default='publication')
    
    def __str__(self):
        return self.title