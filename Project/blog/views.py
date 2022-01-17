## Views are request handlers in Django

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User


## Create dummy data to show in templates
posts = [
    {
        "author" : "meditative-coder",
        "title" : "Blog Post 1",
        "content" : "First post content",
        "date_posted" : "January 12, 2022"
    },
    {
        "author" : "aggresive-coder",
        "title" : "Blog Post 2",
        "content" : "Second post content",
        "date_posted" : "January 11, 2022"
    }
]

def home(request):

    ## Creating a context to pass to template
    ## Every key in this context is accessible in template
    # context = {
    #     'posts' : posts,

    # }
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context=context)


# This view will give list of all blogs
class PostListView(ListView):
    # which model to query
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' # if not given then it passes list of posts with name "object_list"
    ordering = ['-date_posted'] # to present newest posts on top
    paginate_by = 5

# This view is created to filter posts on basis on user (click on username on home page)
class UserPostListView(ListView):
    # which model to query
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' # if not given then it passes list of posts with name "object_list"
    #ordering = ['-date_posted'] # to present newest posts on top
    paginate_by = 5
    
    # 
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# This view will give detail of all blogs
class PostDetailView(DetailView):
    # which model to query
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # which model to query
    model = Post
    fields = ['title','content']

    # set author of post as current logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UserPassesTestMixin -> only allow author to update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # which model to query
    model = Post
    fields = ['title','content']

    # set author of post as current logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # which model to query
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request, 'blog/about.html', {'title':'about'})

