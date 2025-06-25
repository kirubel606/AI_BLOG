from django.db import models

# Create your models here.
class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255,null=True,blank=True)
    title_am = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True,blank=True)
    description_am = models.TextField(blank=True, null=True)