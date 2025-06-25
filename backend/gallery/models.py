from django.db import models

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('DATA_CENTER', 'Data Center'),
        ('SHOWROOM', 'Showroom'),
        ('SUMMER_CAMP', 'Summer Camp'),
        ('MOU', 'MOU'),
    ]
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # ⏱️ Timestamp
    caption = models.CharField(max_length=400, blank=True)
    category = models.CharField( max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True    ) 
    discription = models.TextField(null=True,blank=True)  # 📜 Description


    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"{self.gallery.title} - Image {self.id}"
