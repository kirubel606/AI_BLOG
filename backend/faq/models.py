from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.TextField(null=True,blank=True)
    question_am = models.TextField(null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    answer_am = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.question