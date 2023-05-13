from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from feed.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Post.objects.filter(author=self.get_object().user)
        return context

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return 'user__username'


@login_required
def profile(request):
    posts_list = Post.objects.filter(author=request.user)
    return render(request, 'users/profile.html', {'title': 'profile', 'posts_list': posts_list})


def login(request):
    return render(request, 'users/login.html', {'title': 'login'})


def logout(request):
    return render(request, 'users/logout.html', {'title': 'logout'})


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit-profile.html', context)
