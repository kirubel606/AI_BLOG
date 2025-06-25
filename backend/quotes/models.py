from django.db import models

# Create your models here.
class Quote(models.Model):
    image = models.ImageField(upload_to='quotes/images/')
    quote = models.TextField(blank=True, null=True)
    quote_am = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    name_am = models.CharField(max_length=200,blank=True, null=True)
    position = models.CharField(max_length=100,blank=True, null=True)
    position_am = models.CharField(max_length=100,blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_testimony = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.position}"