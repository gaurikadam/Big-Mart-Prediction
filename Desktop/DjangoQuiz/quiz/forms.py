from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username','email','password1','password2']

