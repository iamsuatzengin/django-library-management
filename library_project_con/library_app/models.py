from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date
# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Language(models.Model):  # book's language
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class Book(models.Model):
    title = models.CharField(max_length=150)
    isbn = models.CharField(
        'ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    about = models.TextField(max_length=1000, blank=True, null=True)
    number_of_page = models.SmallIntegerField()
    book_genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book')
    book_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def short_about(self):
        return self.about[:120] + "..."

    def display_genre(self):
        return ', '.join(i.genre for i in self.book_genre.all()[:3])
    display_genre.short_description = 'Genre'

    class Meta:
        ordering = ['-added_date']

LOAN_STATUS = (
    ('m', 'Maintance'),
    ('o', 'On Loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
)


class BookBorrow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(blank=True, null=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='a',
        help_text='Book availability'
    )

    def __str__(self):
        return "{0} | {1}".format(self.book.title, self.id)

    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
