from django.db import models

# Create your models here.
class Setting(models.Model):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    email = models.EmailField()
    location = models.CharField(max_length=255,blank=True, null=True)
    location_am = models.CharField(max_length=255,blank=True, null=True)
    map_link = models.CharField()
