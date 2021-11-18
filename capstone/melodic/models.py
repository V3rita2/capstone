from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Track(models.Model):

    title = models.CharField(max_length=150)
    cover = models.CharField(max_length=9999, default='No Image')
    body = models.CharField(max_length=9999, default='No body')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tracks")


    def __str__(self):
        return self.title

class Comment(models.Model):

    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.body

