from django.db import models


class TimestampedModel(models.Model):
    """Abstract base model to track created/updated times."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ---------- STARTUP ----------
class Startup(TimestampedModel):
    title_en = models.CharField(max_length=255)
    title_am = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField()
    description_am = models.TextField(blank=True, null=True)

    # for sections like "What is Startup Center?"
    about_en = models.TextField(blank=True, null=True)
    about_am = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_en


class StartupProgram(TimestampedModel):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name="programs")

    title_en = models.CharField(max_length=255)
    title_am = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField()
    description_am = models.TextField(blank=True, null=True)

    duration_en = models.CharField(max_length=100, blank=True, null=True)
    duration_am = models.CharField(max_length=100, blank=True, null=True)

    # icon can be stored as string reference to lucide-react icon name
    icon_name = models.CharField(max_length=100, help_text="e.g. 'Rocket', 'Lightbulb'")

    def __str__(self):
        return f"{self.title_en} ({self.startup.title_en})"


class StartupImage(TimestampedModel):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="startup/images/")
    alt_text_en = models.CharField(max_length=255, blank=True, null=True)
    alt_text_am = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text_en or f"Image for {self.startup.title_en}"


# ---------- TRAINING (Bootcamp + Summer Camp) ----------
class Training(TimestampedModel):
    TRAINING_TYPES = (
        ("bootcamp", "Bootcamp"),
        ("summer_camp", "Summer Camp"),
    )

    training_type = models.CharField(max_length=20, choices=TRAINING_TYPES)

    title_en = models.CharField(max_length=255)
    title_am = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField()
    description_am = models.TextField(blank=True, null=True)

    about_en = models.TextField(blank=True, null=True)
    about_am = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_training_type_display()} - {self.title_en}"


class TrainingProgram(TimestampedModel):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name="programs")

    title_en = models.CharField(max_length=255)
    title_am = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField()
    description_am = models.TextField(blank=True, null=True)

    duration_en = models.CharField(max_length=100, blank=True, null=True)
    duration_am = models.CharField(max_length=100, blank=True, null=True)

    icon_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title_en} ({self.training.get_training_type_display()})"


class TrainingImage(TimestampedModel):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="training/images/")
    alt_text_en = models.CharField(max_length=255, blank=True, null=True)
    alt_text_am = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text_en or f"Image for {self.training.get_training_type_display()} - {self.training.title_en}"
