from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import CreateNewList
from .models import ToDoList, Item

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == 'POST':
        if response.POST.get('save'):
            # when clicked on save button, update the selected checkbox
            for item in ls.item_set.all():
                if response.POST.get('c'+str(item.id)) == 'clicked':
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        elif response.POST.get('newItem'):
            # when clicked on add button, add a new item
            text = response.POST.get('new')
            print("Text = ", text)
            ls.item_set.create(text=text)
            ls.save()

    return render(response, 'main/list.html', {'ls':ls})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            t = ToDoList(title = title)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {'form':form})


def view(response):
    return render(response, 'main/view.html')