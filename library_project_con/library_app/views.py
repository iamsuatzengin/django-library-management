from django.shortcuts import render, redirect
from .models import Book, Author, Genre
from django.views.generic.list import ListView
from django.db.models import Q
# Create your views here.


def search(request):
    search_input = request.GET.get('search_input')
    searched_book = Book.objects.filter(title__icontains=search_input)
    searched_author = Author.objects.filter(
        Q(first_name__icontains=search_input) | Q(last_name__icontains=search_input)
    )
    if searched_book:
        return render(request, 'book_list.html', {'book_list': searched_book})
    if searched_author:
        return render(request, 'author_list.html', {'author_list':searched_author})



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
    return render(request, 'book_detail.html', {'book': book})

class AuthorListView(ListView):
    model = Author
    paginate_by = 20
    template_name='author_list.html'

def author_detail(request, id):
    author = Author.objects.get(id = id)
    return render(request, 'author_detail.html', {'author': author})