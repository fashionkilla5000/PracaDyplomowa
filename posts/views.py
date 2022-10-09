from django.contrib import messages
from .models import Post, LikePost
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timedelta, datetime

from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class PostListView_oczekujace(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/oczekujace.html'  # <posts>/<model>_<viewtype>.html
    login_url = '/login/'
    context_object_name = 'posts'

class PostListView_trasa(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/trasa.html'  # <posts>/<model>_<viewtype>.html
    login_url = '/login/'
    context_object_name = 'posts'

class PostListView_zakonczone(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/zakonczone.html'  # <posts>/<model>_<viewtype>.html
    login_url = '/login/'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = '/login/'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['miasto','adres', 'nr_mieszkania', 'czas_przygotowania', 'płatność', 'kwota', 'telefon', 'komentarz', 'platforma']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.restauracja = self.request.user.restauracja
        # article.save()  # This is redundant, see comments.
        return super(PostCreateView, self).form_valid(form)

    login_url = '/login/'
    success_url = '/'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['adres', 'nr_mieszkania', 'płatność', 'kwota', 'telefon', 'komentarz', 'platforma']
    login_url = '/login/'
    success_url = '/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '/login/'
    success_url = '/post/zakonczone/'


def change_status(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    if post.no_of_likes != None:
        post.trasa = True
        post.zakonczone = False
        post.save()

    return redirect('/')


def change_status_zakoncz(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    post.czas_dostarczenia = datetime.now()
    post.oczekujace = False
    post.trasa = False
    post.zakonczone = True
    post.save()

    return redirect('post/trasa/')

def dodaj_five(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    post.czas_przygotowania = post.czas_przygotowania + 5
    post.save()

    return redirect('/')

def dodaj_ten(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    post.czas_przygotowania = post.czas_przygotowania + 10
    post.save()

    return redirect('/')

def nawiguj(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)

    post.status = 'W trakcie Dostarczania'
    post.save()

    return redirect('https://www.google.com/maps/place/+'+post.adres+',+'+post.miasto)

def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')


    post = Post.objects.get(id=post_id)

    post.czas_odebrania = datetime.now() + timedelta(minutes=post.czas_przygotowania)
    post.save()

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