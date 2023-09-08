from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .filters import PostsFilter
from .forms import PostForm, CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'feed/add_comment.html'
    success_url = reverse_lazy('feed/home')

    def form_valid(self, form):
        post_id = self.kwargs['pk']  # Get the post ID from the URL parameter
        post = get_object_or_404(Post, pk=post_id)  # Get the post instance
        form.instance.post = post  # Associate the comment with the post
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('feed-home')  # Redirect to the home feed after posting a comment

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'feed/about.html', {'title': 'About'})