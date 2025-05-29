import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from categories.models import Category
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify


def upload_to_path(instance: 'News', filename: str) -> str:
    user_id: str = instance.author.id
    news_id: str = instance.id
    return f'{settings.NEWS_IMAGE_DIR_NAME}/{user_id}-{news_id}-{filename}'


class News(models.Model):

    class Meta:
        ordering = ('-created_at',)

    class Status(models.TextChoices):
        DRAFT = 'draft', 'DRAFT'
        PUBLISH = 'publish', 'PUBLISH'

    id = models.CharField(primary_key=True, max_length=36,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    images = models.ImageField(upload_to=upload_to_path, max_length=200, blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category,blank=True,on_delete=models.SET_NULL, null=True,related_name='news_items')
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='news_posts')

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


@receiver(post_delete, sender=News)
def delete_cover_image(sender, instance, **kwargs):
    if instance.cover_image:
        instance.cover_image.delete(save=False)


