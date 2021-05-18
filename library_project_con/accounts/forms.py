from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def forbiddenUsernames(value):
    forbidden_list = [
        'admin', 'user', 'library', 'author', 'book', 'like', 'comment', 'template', 'test',
    ] # etc.
    if value.lower() in forbidden_list:
        raise ValidationError('Invalid username')

def invalidUsername(value):
    if '@' in value or '+' in value or '*' in value or '_' == value[0]:
        raise ValidationError("Invalid username, Don't use these: @, +, *, _ ")


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput())
    last_name = forms.CharField(max_length=50, widget=forms.TextInput())
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(forbiddenUsernames)
        self.fields['username'].validators.append(invalidUsername)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']

