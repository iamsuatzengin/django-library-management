from django.shortcuts import render, redirect
from django.http import HttpResponse

def user_authenticated(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return wrap


def allowed_users(users=[]):
    def decorator(view_func):
        def wraper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in users:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1>You are not authorized</h1>')
        return wraper
    return decorator