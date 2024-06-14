from django.http import JsonResponse
from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()  # a Dict of all the posts
    return render(request, 'posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return JsonResponse(post.serialize())
