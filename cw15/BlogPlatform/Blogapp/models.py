from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.author}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"
