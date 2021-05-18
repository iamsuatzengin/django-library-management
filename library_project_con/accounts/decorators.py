from django.shortcuts import render, redirect


def user_authenticated(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return wrap
