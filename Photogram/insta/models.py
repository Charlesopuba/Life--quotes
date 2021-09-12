from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## Feature to enable posting of photos
class Post(models.Model):
    image = models.ImageField()
    description = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

## Enable commenting on photos
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models .TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateField(auto_now=True)


