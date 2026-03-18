from django.db import models
from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    excerpt = models.TextField()
    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title