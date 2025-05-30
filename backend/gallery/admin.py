from django.contrib import admin
from .models import Gallery, GalleryImage

# Inline for images related to a Gallery
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1  # Number of blank forms

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    inlines = [GalleryImageInline]
