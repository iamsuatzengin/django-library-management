from django.shortcuts import render
from .models import Book, Author, Genre
from django.views.generic.list import ListView
# Create your views here.

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