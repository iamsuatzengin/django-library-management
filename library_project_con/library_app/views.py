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
    paginate_by = 21
    template_name = 'book_list.html'

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})