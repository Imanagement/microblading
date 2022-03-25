from django.urls import path, re_path
from .views import PostListView, PostDetailView, PostCategoryListView, redirect_to_blog_home, search_view

app_name = 'blog'
urlpatterns = [
    path('search/', search_view, name="search"),
    path('category', redirect_to_blog_home, name="redirect-to-blog-home"),
    path('', PostListView.as_view(), name="blog-index"),
    path('post/<slug>', PostDetailView.as_view(), name="blog-detail"),
    path('category/<slug>', PostCategoryListView.as_view(), name="blog-category-list"),
    re_path(r'^category(\/){0,1}', redirect_to_blog_home, name="redirect-to-blog-home")
]