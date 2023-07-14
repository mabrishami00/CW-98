from django.urls import path
from .views import home, post_list, post_details


urlpatterns = [
    path("home/", home),
    path("post/", post_list),
    path("post/<int:pk>/", post_details, name="post_details"),
]
