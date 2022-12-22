from django.views.generic import ListView, DetailView

from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
