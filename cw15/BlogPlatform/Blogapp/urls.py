from django.urls import path
from .views import (
    home,
    post_list,
    author_list,
    post_details,
    author_details,
    category_list,
    category_details,
)


urlpatterns = [
    path("", home, name="home"),
    path("post/", post_list, name="post"),
    path("post/<int:pk>/", post_details, name="post_details"),
    path("author/", author_list, name="author"),
    path("author/<int:pk>/", author_details, name="author_details"),
    path("category/", category_list, name="category"),
    path("category/<int:pk>/", category_details, name="category_details"),
]
