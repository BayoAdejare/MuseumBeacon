from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    collection = models.TextField()
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
