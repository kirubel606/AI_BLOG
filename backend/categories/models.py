from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    name_am = models.CharField(max_length=300,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    description_am = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='categories/')
    is_core = models.BooleanField(default=False)

    def __str__(self):
        return self.name