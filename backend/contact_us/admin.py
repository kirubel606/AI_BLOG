from django.contrib import admin

# Register your models here.
from .models import ContactUs
from .models import EmailSubscription

class UserAdmin(admin.ModelAdmin):
    model = ContactUs
admin.site.register(ContactUs, UserAdmin)
admin.site.register(EmailSubscription, UserAdmin)
