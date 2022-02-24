"""views file"""
from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """List Views class"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
