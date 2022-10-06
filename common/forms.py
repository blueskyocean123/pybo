from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    # This is needed to use is_valid function in UserCreationForm Class
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")