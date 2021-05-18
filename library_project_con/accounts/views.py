from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import user_authenticated
from django.contrib.auth.models import User
from .models import Profile
from library_app.models import Book
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

@user_authenticated
def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully')
        return redirect('login')
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Your password was successfully updated!')
        return redirect('change_password')
    return render(request, 'change_password.html', {'form':form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def favorite(request, id):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    profile = Profile.objects.get(user=request.user)

    if profile in book.favorites.all():
        book.favorites.remove(profile)
    else:
        book.favorites.add(profile)
    return HttpResponseRedirect(reverse('book_detail', args=[str(id)]))

@login_required(login_url='login')
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user__id = user.id)
    form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update_profile.html', {'form': form})