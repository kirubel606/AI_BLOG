from django.db import models
from categories.models import Category

# Create your models here.
class Resource(models.Model):
    CLASSIFICATION_CHOICES = [
     ('publication', 'Publication'),
     ('resource', 'Resource'),
     ('case_study', 'Case Study'),
     ('development', 'Development'),
     ('patents', 'Patents'),
     ('dataset', 'Dataset'),
     ('tool', 'Tool'),
    ]
    title = models.CharField(max_length=255,blank=True, null=True)
    title_am = models.CharField(max_length=255,blank=True, null=True)
    author = models.CharField(max_length=100,blank=True, null=True)
    author_am = models.CharField(max_length=200,blank=True, null=True)
    published_at = models.DateField()
    plublisher = models.CharField(max_length=100,null=True)
    plublisher_am = models.CharField(max_length=200,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=255)
    classification = models.CharField(max_length=20,choices=CLASSIFICATION_CHOICES,default='publication')
    
    def __str__(self):
        return self.title