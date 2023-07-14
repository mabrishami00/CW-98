from django.urls import path
from .views import home, post_list


urlpatterns = [path("home/", home), path("post/", post_list)]
