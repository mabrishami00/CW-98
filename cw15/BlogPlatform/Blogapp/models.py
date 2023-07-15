from django.db import models
from Categoryapp.models import Category

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    # image = models.ImageField(upload_to="post_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    publication_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author},{self.post.title}"
