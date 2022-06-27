from django.urls import path

from .views.blog.post_views import (HomeView, PostDetail, AddPostView, UpdatePostView, DeletePostView, post_like)
from .views.blog.category_views import (CategoriesListView, CategoryPostsListView, CategoryCreateView, CategoryUpdateCreateView)

app_name = 'blog'

urlpatterns = [
    # POST URLS #
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add-post', AddPostView.as_view(), name='add_post'),
    path('<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('<int:pk>/like', post_like, name='post_like'),


    # CATEGORY URLS #
    path('categories', CategoriesListView.as_view(), name='category_list'),
    path('categories/<str:slug>/posts', CategoryPostsListView.as_view(), name='category_posts'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:slug>/update', CategoryUpdateCreateView.as_view(), name='category_update'),
]