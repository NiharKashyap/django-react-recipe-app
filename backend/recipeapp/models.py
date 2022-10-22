from django.db import models
from django.contrib.auth.models import User

class RecipeModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image_url=models.URLField(null=True)
