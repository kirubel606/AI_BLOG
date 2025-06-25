from django.contrib import admin
from .models import Gallery, GalleryImage

# Inline for images related to a Gallery
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1  # Number of blank forms

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_am', 'category', 'created_at']
    search_fields = ['title', 'title_am', 'caption', 'caption_am']
    list_filter = ['category', 'created_at']
    inlines = [GalleryImageInline]
    fieldsets = (
        (None, {
            'fields': (
                'title', 'title_am',
                'caption', 'caption_am',
                'discription', 'discription_am',
                'category'
            )
        }),
    )

def image_count(self, obj):
    return obj.images.count()
image_count.short_description = 'Image Count'


