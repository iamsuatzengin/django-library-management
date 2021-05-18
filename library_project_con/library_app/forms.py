from django import forms
from .models import BookComments, Book, Author

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