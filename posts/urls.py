from django.urls import path
from .views import (
    PostListView_oczekujace,
    PostListView_trasa,
    PostListView_zakonczone,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostStreamView,
)

urlpatterns = [
    path('', PostListView_oczekujace.as_view(), name='posts-home'),
    path('stream/', PostStreamView.as_view(), name='stream'),
    path('post/trasa/', PostListView_trasa.as_view(), name='posts-trasa'),
    path('post/zakonczone/', PostListView_zakonczone.as_view(), name='posts-zakonczone'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]