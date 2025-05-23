from django.contrib import admin

# Register your models here.
from .models import RND

class UserAdmin(admin.ModelAdmin):
    model = RND
admin.site.register(RND, UserAdmin)
