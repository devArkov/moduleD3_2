from django.views.generic import ListView, DetailView

from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-created_at')


class NewsDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
