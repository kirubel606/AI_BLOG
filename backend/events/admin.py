from django.contrib import admin
from .models import Event, EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Number of extra blank forms

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    list_display = ('title', 'location', 'start_date', 'end_date', 'status')
