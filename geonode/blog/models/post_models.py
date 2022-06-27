from django.utils import timezone

from django.db import models
from django.conf import settings

class Post(models.Model):
    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


