from django.contrib import admin

# Register your models here.
from .models import AboutUs,Person,OrganizationUnit

class UserAdmin(admin.ModelAdmin):
    model = AboutUs
admin.site.register(AboutUs, UserAdmin)
admin.site.register(Person)
admin.site.register(OrganizationUnit)
