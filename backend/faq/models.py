from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
