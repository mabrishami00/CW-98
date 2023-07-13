from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, "home.html")

def show_post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})