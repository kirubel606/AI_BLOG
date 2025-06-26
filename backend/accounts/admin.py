from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username','is_admin', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active','is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_admin', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
        ('Profile', {'fields': ('profile_image',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active','is_admin')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
