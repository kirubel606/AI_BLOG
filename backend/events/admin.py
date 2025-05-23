from django.contrib import admin

# Register your models here.
from .models import Event

class UserAdmin(admin.ModelAdmin):
    model = Event
admin.site.register(Event, UserAdmin)
