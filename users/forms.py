from django import forms
from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username','is_driver','is_restaurator', 'password1', 'password2']
