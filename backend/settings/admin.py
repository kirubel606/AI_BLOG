from django.contrib import admin

# Register your models here.
from .models import Setting

class UserAdmin(admin.ModelAdmin):
    model = Setting
admin.site.register(Setting, UserAdmin)
