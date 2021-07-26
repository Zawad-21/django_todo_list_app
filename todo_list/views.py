from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import *
from .forms import Todo_form, Create_user_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# view for the main page
@login_required(login_url='login')
def home(request):
    todos = Todo.objects.filter(user = request.user)
    form = Todo_form()
    if request.method == 'POST':
        form = Todo_form(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            return redirect('home')
    context = {'todos': todos, 'form': form}
    return render(request, 'todo_list/main.html', context)


def register_page(request):
    form = Create_user_form()
    if request.method == 'POST':
        form = Create_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(
                request, 'Account successfully created ' + username)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'todo_list/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'todo_list/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')

