from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Borrowing, Book, Reader

def index(request):
    template = loader.get_template("dbapp/index.html")
    context = { 'message' : "Welcome in my db app" }
    return HttpResponse(template.render(context, request))

def borrowings(request):
    template = loader.get_template("dbapp/list.html")
    found = list()
    try:
        fillFound(request.GET.get('keyword'), Borrowing, found)
    except:
        print("no keyword")

    context = { 'objects_list' : Borrowing.objects.all(),
    'found' : found }
    return HttpResponse(template.render(context, request))

def books(request):
    template = loader.get_template("dbapp/list.html")
    found = list()
    try:
        fillFound(request.GET.get('keyword'), Book, found)
    except Exception as e:
        print(e)
        print("no keyword")

    context = { 'objects_list' : Book.objects.all(),
    'found' : found }
    return HttpResponse(template.render(context, request))

def readers(request):
    template = loader.get_template("dbapp/list.html")
    found = list()
    try:
        fillFound(request.GET.get('keyword'), Reader, found)
    except:
        print("no keyword")

    context = { 'objects_list' : Reader.objects.all(),
    'found' : found }
    return HttpResponse(template.render(context, request))

def fillFound(keyword, model, found):
    for entry in model.objects.all():
        if keyword in str(entry):
            if model is Book:
                found.append(entry.isbn)
            else:
                found.append(entry.id)
