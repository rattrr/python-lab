from django.shortcuts import render
from django.http import HttpResponse

def index_form(request):
    return render(request, "form.html")

def form_response(request):
    if 'test' in request.GET:
        return render(request, "form_response.html")
    else:
        return HttpResponse("You typed nothing")
