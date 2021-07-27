from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


# Create your views here.
def register(request):
    return HttpResponse
def login(request):
    return HttpResponse
def trash(request):
    return HttpResponse
def emptyTrash(request):
    return HttpResponse
def archiveTodo(request):
    return HttpResponse
def getTrash(request):
    return HttpResponse
def getArchived(request):
    return HttpResponse

@api_view(['GET'])
def getTodos(request):
    todo = Todo.objects.all()
    context =  TodoSerializer(todo, many=True)
    return Response(context.data)