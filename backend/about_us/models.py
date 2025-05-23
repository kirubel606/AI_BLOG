from django.db import models

# Create your models here.
class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255)
    description = models.TextField()
