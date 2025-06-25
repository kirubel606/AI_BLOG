from django.contrib import admin
from .models import Vacancy



@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title','title_am', 'created_at']
    search_fields = ['title','title_am', 'description','description_am']
    list_filter = ['created_at']