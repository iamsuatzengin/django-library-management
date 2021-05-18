from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book, Author, Genre, BookComments
from .forms import BookCommentsForm, BookForm, AuthorForm
from accounts.decorators import allowed_users


def search(request):
    search_input = request.GET.get('search_input')
    searched_book = Book.objects.filter(title__icontains=search_input)
    searched_author = Author.objects.filter(
        Q(first_name__icontains=search_input) | Q(
            last_name__icontains=search_input)
    )
    if searched_book:
        return render(request, 'book_list.html', {'book_list': searched_book})
    if searched_author:
        return render(request, 'author_list.html', {'author_list': searched_author})


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'index.html', context)


class BookListView(ListView):
    model = Book
    paginate_by = 20
    template_name = 'book_list.html'


def book_detail(request, id):
    book = Book.objects.get(id=id)
    form = BookCommentsForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.book = book
        comment.user = request.user
        comment.save()
        return HttpResponseRedirect(reverse('book_detail', args=[str(id)]))

    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'book_detail.html', context)


class AuthorListView(ListView):
    model = Author
    paginate_by = 20
    template_name = 'author_list.html'


def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'author_detail.html', {'author': author})


@login_required(login_url='login')
@allowed_users(['librarian'])
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'add_book.html', {'form': form})


@login_required(login_url='login')
@allowed_users(['librarian'])
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')


@login_required(login_url='login')
@allowed_users(['librarian'])
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('book_detail', args=[str(id)]))
    return render(request, 'update_book.html', {'form': form})


@login_required(login_url='login')
@allowed_users(['librarian'])
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, 'add_author.html', {'form': form})


@login_required(login_url='login')
@allowed_users(['librarian'])
def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('author_list')


@login_required(login_url='login')
@allowed_users(['librarian'])
def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('author_detail', args=[str(id)]))
    return render(request, 'update_author.html', {'form': form})

