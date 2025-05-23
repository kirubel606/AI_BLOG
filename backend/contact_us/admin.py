from django.contrib import admin

# Register your models here.
from .models import ContactUs

class UserAdmin(admin.ModelAdmin):
    model = ContactUs
admin.site.register(ContactUs, UserAdmin)
