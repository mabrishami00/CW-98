from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def home(request):
    return render(request, "home.html")


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_details.html", {"post": post})
