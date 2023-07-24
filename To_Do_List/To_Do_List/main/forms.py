from django import forms
from .models import ToDoList, Items
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = [
            'name'
        ]


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'text', 'description', 'complete'
        ]
