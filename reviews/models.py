from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    like_users = models.ManyToManyField(get_user_model(), related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content