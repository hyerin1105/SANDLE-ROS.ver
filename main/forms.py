from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=("password",)

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")