from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
