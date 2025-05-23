from django.contrib import admin

# Register your models here.
from .models import Resource

class UserAdmin(admin.ModelAdmin):
    model = Resource
admin.site.register(Resource, UserAdmin)
