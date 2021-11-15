from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Track(models.Model):

    title = models.CharField(max_length=150)
    cover = models.CharField
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return self.title
