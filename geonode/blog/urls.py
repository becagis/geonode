from django.urls import path

from .views.blog.article_views import (HomeView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]