from django.contrib import admin

# Register your models here.
from .models import FAQ

class UserAdmin(admin.ModelAdmin):
    model = FAQ
admin.site.register(FAQ, UserAdmin)
