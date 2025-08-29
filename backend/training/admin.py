from django.contrib import admin
from .models import (
    Startup, StartupProgram, StartupImage,
    Training, TrainingProgram, TrainingImage
)

# ---------- STARTUP ----------
@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_am", "created_at", "updated_at")
    search_fields = ("title_en", "title_am")


@admin.register(StartupProgram)
class StartupProgramAdmin(admin.ModelAdmin):
    list_display = ("title_en", "startup", "duration_en", "created_at")
    search_fields = ("title_en", "startup__title_en")


@admin.register(StartupImage)
class StartupImageAdmin(admin.ModelAdmin):
    list_display = ("alt_text_en", "startup", "created_at")
    search_fields = ("alt_text_en", "startup__title_en")


# ---------- TRAINING ----------
@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title_en", "training_type", "created_at", "updated_at")
    list_filter = ("training_type",)
    search_fields = ("title_en", "title_am")


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ("title_en", "training", "duration_en", "created_at")
    search_fields = ("title_en", "training__title_en")


@admin.register(TrainingImage)
class TrainingImageAdmin(admin.ModelAdmin):
    list_display = ("alt_text_en", "training", "created_at")
    search_fields = ("alt_text_en", "training__title_en")
