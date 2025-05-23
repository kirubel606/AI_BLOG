from django.contrib import admin

# Register your models here.
from .models import News

class UserAdmin(admin.ModelAdmin):
    model = News
admin.site.register(News, UserAdmin)
