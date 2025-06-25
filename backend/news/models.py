import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from categories.models import Category
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import URLValidator


class News(models.Model):

    class Meta:
        ordering = ('-created_at',)

    class Status(models.TextChoices):
        DRAFT = 'draft', 'DRAFT'
        PUBLISH = 'publish', 'PUBLISH'

    id = models.CharField(primary_key=True, max_length=36,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=225, unique=True,null=True, blank=True)
    title_am = models.CharField(max_length=225, unique=True,null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    subtitle_am = models.CharField(max_length=300, null=True, blank=True)
    cover_image = models.ImageField(upload_to='news/', max_length=200, blank=True, null=True)
    
    iframe = models.TextField(blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    content_am = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,blank=True,on_delete=models.SET_NULL, null=True,related_name='news_items')
    tags = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='news_posts')
    
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title



class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.news.title}"


@receiver(post_delete, sender=News)
def delete_cover_image(sender, instance, **kwargs):
    if instance.cover_image:
        instance.cover_image.delete(save=False)


@receiver(post_delete, sender=NewsImage)
def delete_news_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)