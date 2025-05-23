from django.contrib import admin

# Register your models here.
from .models import Category

class UserAdmin(admin.ModelAdmin):
    model = Category
admin.site.register(Category, UserAdmin)
