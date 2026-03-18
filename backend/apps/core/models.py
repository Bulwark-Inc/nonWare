from django.db import models
from apps.common.models import TimeStampedModel


class Skill(TimeStampedModel):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="1–100")

    def __str__(self):
        return self.name
    
class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField(default=list)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Service(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_range = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title