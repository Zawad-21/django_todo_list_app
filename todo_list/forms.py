from django import forms
from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Todo_form(ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)


class Create_user_form(UserCreationForm):
    password2 = None
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']