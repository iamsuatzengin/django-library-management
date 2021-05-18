from django.contrib import admin
from .models import Book, BookBorrow, Author, Genre, Language, BookComments
# Register your models here.


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookComments)

class BookBorrowInline(admin.TabularInline):
    model = BookBorrow
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'author')
    inlines = [BookBorrowInline]


@admin.register(BookBorrow)
class BookBorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    exclude = ('about', 'book_language', 'isbn')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
