from django.db import models
from apps.common.models import TimeStampedModel


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    
class QuoteRequest(TimeStampedModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    project_type = models.CharField(max_length=150)
    budget = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.project_type}"