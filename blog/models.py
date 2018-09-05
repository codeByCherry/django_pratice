from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,
                               related_name='blogArticles',
                               on_delete=models.CASCADE,
                               )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
