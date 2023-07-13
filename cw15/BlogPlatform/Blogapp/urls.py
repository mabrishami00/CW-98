from django.urls import path
from .views import home, show_post


urlpatterns = [path("", home), path("post/", show_post)]
