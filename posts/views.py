from django.contrib import messages
from .models import Post, LikePost
from users.models import CustomUser
from django.shortcuts import render, redirect
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
#     return render(request, 'posts/oczekujace.html', context)
#

class PostListView_oczekujace(ListView):
    model = Post
    template_name = 'posts/oczekujace.html'  # <posts>/<model>_<viewtype>.html
    context_object_name = 'posts'

class PostListView_trasa(ListView):
    model = Post
    template_name = 'posts/trasa.html'  # <posts>/<model>_<viewtype>.html
    context_object_name = 'posts'

class PostListView_zakonczone(ListView):
    model = Post
    template_name = 'posts/zakonczone.html'  # <posts>/<model>_<viewtype>.html
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['adres', 'payment', 'amount','phone', 'comment', 'platform']
    success_url = '/'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['adres', 'payment', 'amount','phone', 'comment', 'platform']
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


def change_status(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    if post.no_of_likes != None:
        post.oczekujace = False
        post.trasa = True
        post.zakonczone = False
        post.save()

    return redirect('/')

def change_status_zakoncz(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    post.oczekujace = False
    post.trasa = False
    post.zakonczone = True
    post.save()

    return redirect('post/trasa/')

def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')


    post = Post.objects.get(id=post_id)


    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = username


        post.save()

        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = None
        post.status = 'oczekujace'


        post.save()
        return redirect('/')