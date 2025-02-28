from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
    }

    return render(
        request,
        'index.html',
        context,
    )


def post(request, slug):
    p = Post.objects.filter(
        slug=slug,
    ).first()
    context = {
        'post': p,
    }
    return render(
        request,
        'post.html',
        context,
    )


def get_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.all()
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})