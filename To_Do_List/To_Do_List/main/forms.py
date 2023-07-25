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
            'username': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'eg paloaks'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ToDoListForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        owner = cleaned_data.get('owner')
        if owner is None:
            cleaned_data['owner'] = self.user
        return cleaned_data


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'text', 'description'
        ]
