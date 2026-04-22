from django.db import models

# Create your models here.

class PostHistory(models.Model):
    raw_thought = models.TextField()
    tone = models.CharField(max_length=100)
    audience = models.CharField(max_length=100)
    generated_post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tone} - {self.created_at.date()}"
