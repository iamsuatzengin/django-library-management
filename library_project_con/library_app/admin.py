from django.contrib import admin
from .models import Book, BookBorrow, Author, Genre, Language
# Register your models here.
admin.site.register(Book)
admin.site.register(BookBorrow)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)