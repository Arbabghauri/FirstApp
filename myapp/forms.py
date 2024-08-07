from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = AppUser
        fields = ["email", "username", "password1", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
