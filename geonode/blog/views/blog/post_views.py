from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from geonode.blog.forms import PostForm, EditForm
from geonode.blog.models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/post/home.html'
    ordering = ['-date_created']

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        liked = False
        post = get_object_or_404(Post, pk=self.kwargs['pk'])

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        content['total_likes'] = post.total_likes()
        content['liked'] = liked
        return content


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/add_post.html'
    # fields = '__all__' # ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/post/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post/delete_post.html'
    success_url = reverse_lazy('home')

def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog:post_detail', args=[str(pk)]))