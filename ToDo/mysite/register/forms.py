from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import EmailField

class RegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
