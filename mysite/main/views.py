from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>Id = %s, name = %s" % (id, ls.title))

def v1(response):
    return HttpResponse("<h1>View 1</h1>")