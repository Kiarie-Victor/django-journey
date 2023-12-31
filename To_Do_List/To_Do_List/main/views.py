from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ToDoListForm, SignUpForm, ItemsForm
from django.contrib.auth import login, logout, authenticate
from .models import ToDoList
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def home(request):
    todolist=None
    try:
        todolist = ToDoList.objects.get(owner=request.user)
        return redirect('/view')
    except:
        pass
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            tdlist = form.save(commit=False)
            tdlist.owner = request.user
            tdlist.save()
            return redirect('/add-items')
    else:
        form = ToDoListForm()
    return render(request, 'main/add_items.html', {'form': form, 'todolist': todolist})


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
        form = ItemsForm(request.POST)
        if form.is_valid():
            items = form.save(commit=False)
            # Get the ToDoList instance associated with the user
            items.author = get_object_or_404(ToDoList, owner=request.user)
            items.save()
            return redirect('/view')
    else:
        form = ItemsForm()
    return render(request, 'main/add_items.html', {'form': form, 'todolist': todolist})


@login_required(login_url='login')
def display(request):
    todolist = ToDoList.objects.get(owner=request.user)
    return render(request, 'main/view.html', {'todolist': todolist})
