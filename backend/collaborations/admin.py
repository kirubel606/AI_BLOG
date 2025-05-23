from django.contrib import admin

# Register your models here.
from .models import Collaboration

class UserAdmin(admin.ModelAdmin):
    model = Collaboration
admin.site.register(Collaboration, UserAdmin)
