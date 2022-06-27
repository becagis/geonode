from django.urls import reverse
from django.utils import timezone

from django.db import models
from django.conf import settings
from .category_models import Category


class Post(models.Model):
    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    views = models.PositiveIntegerField(default=0)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()



