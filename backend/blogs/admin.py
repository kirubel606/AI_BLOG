from django.contrib import admin

# Register your models here.
from .models import Blog

class UserAdmin(admin.ModelAdmin):
    model = Blog
admin.site.register(Blog, UserAdmin)
