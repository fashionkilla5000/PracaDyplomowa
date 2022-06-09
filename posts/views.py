from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# def home(request):
#     context = {
#         'posts': Posts.objects.all()
#     }
#     return render(request, 'posts/home.html', context)
#

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'  # <posts>/<model>_<viewtype>.html
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['adres', 'payment', 'amount', 'phone', 'comment', 'platform', 'status']
    success_url = '/'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['adres', 'payment', 'amount', 'phone', 'comment', 'platform', 'status']
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'