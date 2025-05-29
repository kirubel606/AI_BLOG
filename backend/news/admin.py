from django.contrib import admin
from .models import News, NewsImage  # ✅ import both models


class NewsImageInline(admin.TabularInline):  # or admin.StackedInline for more detail
    model = NewsImage
    extra = 1  # how many empty forms to show initially
    fields = ('image',)
    readonly_fields = ()
    can_delete = True


class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [NewsImageInline]  # ✅ attach the inline
    list_display = ('title', 'status', 'created_at')  # optional, for better admin view
    search_fields = ('title', 'subtitle', 'content')  # optional
    list_filter = ('status', 'category', 'created_at')  # optional


admin.site.register(News, NewsAdmin)
