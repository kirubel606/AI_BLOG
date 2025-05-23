from django.db import models

# Create your models here.
class Collaboration(models.Model):
    logo = models.ImageField(upload_to='collaborations/')
    category = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.category