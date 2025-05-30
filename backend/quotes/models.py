from django.db import models

# Create your models here.
class Quote(models.Model):
    image = models.ImageField(upload_to='quotes/images/')
    quote = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    is_testimony = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.position}"