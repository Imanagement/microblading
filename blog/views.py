from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Category


class BaseListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostListView(BaseListView):
    template_name = 'blog/pages/post-list.html'
    paginate_by = 10
    model = Post

    def get_queryset(self):
        return super().get_queryset().select_related('author').select_related('category').prefetch_related('image')


class PostDetailView(DetailView):
    template_name = 'blog/pages/post-detail.html'
    model = Post

    def get_queryset(self):
        return super().get_queryset().select_related('category').select_related('author')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostCategoryListView(BaseListView):
    template_name = 'blog/pages/post-list.html'
    paginate_by = 10
    model = Post

    def get_queryset(self):
        if self.kwargs['slug'] != 'uncategorized':
            return super().get_queryset().filter(category__slug=self.kwargs['slug'])
        else:
            return super().get_queryset().filter(category__isnull=True)


def search_view(request):
    if request.GET:
        query_string = request.GET['s']
        if len(query_string) <= 0:
            return redirect('blog:blog-index')
        queryset = Post.objects.filter(name__icontains=query_string)
        queryset |= Post.objects.filter(category__name__icontains=query_string)
        queryset |= Post.objects.filter(body__icontains=query_string)

        context = {
            'post_list': queryset,
            'categories': Category.objects.all()
        }

        return render(request, 'blog/pages/post-list.html', context)

    else:
        return redirect('blog:blog-index')


def redirect_to_blog_home(request, regex=None):
    return redirect('blog:blog-index')
