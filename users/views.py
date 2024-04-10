from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.urls import reverse_lazy
from .models import UserProfile
from posts.models import Post


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('posts:list')

@login_required
def profile(request, username):
    try:
        user_profile = UserProfile.objects.get(user__username=username)
        user_posts = user_profile.posts.filter(author=user_profile.user)  # Фильтруем по автору, используя объект пользователя
        return render(request, 'users/profile.html', {'user_profile': user_profile, 'user_posts': user_posts})
    except UserProfile.DoesNotExist:
        return render(request, 'users/profile.html', {'error_message': 'User profile not found'})