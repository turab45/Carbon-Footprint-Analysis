from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import CreateNewList
from .models import ToDoList, Item

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'main/list.html', {'ls':ls})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            t = ToDoList(title = title)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {'form':form})