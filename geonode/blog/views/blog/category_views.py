from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from geonode.blog.models import Category, Post

class CategoriesListView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'categories'
    template_name = 'blog/category/categories_list.html'

    def get_queryset(self):
        return Category.objects.order_by('-date_created')


class CategoryPostsListView(ListView):
    model = Post
    paginate_by = 12
    context_object_name = 'posts'
    template_name = 'blog/category/category_posts.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Post.objects.filter(category=category, status=Post.PUBLISHED)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostsListView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['category'] = category
        return context


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = [
        'name',
        # 'image'
    ]
    template_name = 'blog/category/category_form.html'

    def form_valid(self, form):
        form.instance.save()
        messages.success(self.request, f"'{form.instance.name}' "
                                       f"submitted successfully. You will be "
                                       f"notified when it is approved."
                                       f"Thank you !!!")
        return redirect('/')


class CategoryUpdateCreateView(LoginRequiredMixin, SuccessMessageMixin,
                               UpdateView):
    model = Category
    fields = [
        'name',
        # 'image'
    ]
    template_name = 'blog/category/category_form.html'
    success_url = reverse_lazy("blog:categories_list")
    success_message = "Category Updated Successfully"