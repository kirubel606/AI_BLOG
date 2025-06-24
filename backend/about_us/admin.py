from django.contrib import admin

# Register your models here.
from .models import AboutUs

class UserAdmin(admin.ModelAdmin):
    model = AboutUs
admin.site.register(AboutUs, UserAdmin)
