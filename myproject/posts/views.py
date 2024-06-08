from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()  # a Dict of all the posts
    return render(request, 'posts_list.html', {'posts': posts})
