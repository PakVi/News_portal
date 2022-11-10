from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
# def default(request):
#     posts=Post.objects.all()
#     return render(request, 'default.html', context={'posts':posts})

class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostsDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'posts'