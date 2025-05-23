from django.db import models

class RND(models.Model):
    TYPE_CHOICES = [
        ('research', 'Research'),
        ('development', 'Development'),
        ('case_study', 'Case Study'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    link = models.URLField()
    images = models.ImageField(upload_to='rnd/')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True) 
    tags = models.CharField(max_length=255, null=True)
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='research',
    )

    def __str__(self):
        return self.title
