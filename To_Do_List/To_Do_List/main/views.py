from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ToDoListForm, SignUpForm, ItemsForm
from django.contrib.auth import login, logout, authenticate
from .models import ToDoList
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def home(request):
    todolist = ToDoList.objects.all()

    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        tdlist = form.save()
        # tdlist.owner = request.user
        # tdlist.save()
        return redirect('/add_items')
    else:
        form = ToDoListForm()
    return render(request, 'main/home.html', {'form': form, 'todolist': todolist})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def add_items(request):
    todolist = ToDoList.objects.all()
    if request.method == 'POST':
        form = Items(request.POST)
        if form.is_valid:
            items = form.save(commit=False)
            items.author = request.user
            items.save()
            return redirect('/home')
    else:
        form = ItemsForm()
    return render(request, 'main/add_items.html', {'form': form, 'todolist': todolist})
