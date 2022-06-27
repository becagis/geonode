from django.views.generic import ListView, DetailView
from geonode.blog.models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/post/home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'