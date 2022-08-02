from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    all = Todo.objects.all()

    return render(request, 'home.html', {'all': all} )


def say_hello(request):

    return render(request, 'hello.html')

def detail(request, id):
    todo = Todo.objects.get(id= id)
    return render(request, 'detail.html', {'todo':todo})

def delete(request, id):
     Todo.objects.get(id= id).delete()
     messages.success(request, 'Todo deleted successfully', extra_tags= 'success')
     return redirect('Home')


def kaka(request, id):
    todo = Todo.objects.get(id= id)
    return render(request, 'base.html', {'todo':todo})

def create (request ):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'], body = cd['body'], email = cd['email'], created =cd['created'])
            messages.success(request,'Todo Create Successfully', extra_tags= 'success')
            return redirect('Home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, id):
    todo= Todo.objects.get(id=id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('details', id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})