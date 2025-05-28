from django.db import models
from categories.models import Category

# Create your models here.
class Collaboration(models.Model):
    logo = models.ImageField(upload_to='collaborations/')
    category = models.ForeignKey(Category,blank=True,on_delete=models.SET_NULL, null=True,related_name='collab_items')
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.category.name if self.category else "No Category"