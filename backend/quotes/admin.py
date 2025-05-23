from django.contrib import admin

# Register your models here.
from .models import Quote

class UserAdmin(admin.ModelAdmin):
    model = Quote
admin.site.register(Quote, UserAdmin)
