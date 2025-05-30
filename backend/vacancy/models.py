from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    google_form_link = models.URLField()
    location = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # 🕒 Timestamp

    def __str__(self):
        return self.title
