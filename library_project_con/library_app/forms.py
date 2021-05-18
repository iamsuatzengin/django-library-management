from django import forms
from .models import BookComments


class BookCommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }), label='Comment')

    class Meta:
        model = BookComments
        fields = ['body']