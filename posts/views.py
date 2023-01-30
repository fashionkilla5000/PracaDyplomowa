import json
from django.utils.formats import localize
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import StreamingHttpResponse
from django.views import View
import time
from .models import Post, KtoDostarcza, Restauracja
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
    fields = ['adres', 'nr_mieszkania', 'czas_przygotowania', 'płatność', 'kwota', 'telefon', 'komentarz', 'platforma']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.restaurant = self.request.user.restaurant
        post.miasto = self.request.user.restaurant.miasto
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

    if post.zabrane_przez != None:
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

def zabierz(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    post.czas_odebrania = datetime.now() + timedelta(minutes=post.czas_przygotowania)
    post.save()

    zabierz_filter = KtoDostarcza.objects.filter(post_id=post_id, username=username).first()

    if zabierz_filter == None:
        nowy_zabieracz = KtoDostarcza.objects.create(post_id=post_id, username=username)
        nowy_zabieracz.save()
        post.zabrane_przez = username
        post.status = 'oczekujace'

        post.save()

        return redirect('/')
    else:
        zabierz_filter.delete()
        post.zabrane_przez = None
        post.oczekujace = True
        post.trasa = False


        post.save()
        return redirect('/')

def event_stream():

    initial_data = ""
    while True:
        data = json.dumps(list(Post.objects.order_by("-id").values("id","adres","nr_mieszkania","date",
                                        "restaurant__nazwa", "czas_przygotowania","czas_odebrania","zabrane_przez","status",
                                                                   "trasa","zakonczone")), cls=DjangoJSONEncoder)

        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data)
            initial_data = data
        time.sleep(1)

class PostStreamView(View):

    def get(self, request):
        response = StreamingHttpResponse(event_stream())
        response['Content-Type'] = 'text/event-stream'
        return response