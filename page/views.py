from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Coming up")
def todo(request):
    template="todo.html"
    context={}
    return render(request,template,context)
def login(request):
    return HttpResponse("Coming up")
def register(request):
    template="registration.html"
    context={}
    return render(request,template,context)