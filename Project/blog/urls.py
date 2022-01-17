## URL's for Blog app

from django.urls import path
from . import views
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


## part of url string after /blog/ will come here
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #This view looks for an template of name of format <app>/<model>_<viewtype>.html
    # path('', views.home, name='blog-home') # uncomment to work with function based view,
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]