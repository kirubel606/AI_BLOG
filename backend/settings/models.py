from django.db import models

# Create your models here.
class Setting(models.Model):
    line1 = models.CharField(max_length=255,null=True,blank=True)
    line2 = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    linkdin = models.URLField(null=True,blank=True)
    location = models.CharField(max_length=255,blank=True, null=True)
    location_am = models.CharField(max_length=255,blank=True, null=True)
    map_link = models.CharField(max_length=255)
