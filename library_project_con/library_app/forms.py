from django import forms
from .models import BookComments, Book, Author, Language, Genre
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'isbn', 'about', 'number_of_page',
            'book_genre', 'book_language', 'author', 'book_image',
        ]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'first_name', 'last_name',
            'date_of_birth', 'date_of_death', 'about', 'author_image'
        ]

class BookCommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }), label='Comment')

    class Meta:
        model = BookComments
        fields = ['body']


def unique_genre(value):
    if Genre.objects.filter(genre__iexact=value).exists():
        raise ValidationError('The named {} genre already exists!'.format(value))

def unique_language(value):
    if Language.objects.filter(language__iexact=value).exists():
        raise ValidationError('This language already exists!')

class GenreForm(forms.ModelForm):
    genre = forms.CharField(widget=forms.TextInput(), validators=[unique_genre])
    class Meta:
        model = Genre
        fields = ['genre']

class LanguageForm(forms.ModelForm):
    language = forms.CharField(widget=forms.TextInput(), validators=[unique_language])
    class Meta:
        model = Language
        fields = ['language']