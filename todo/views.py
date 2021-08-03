from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.parsers import FormParser
from rest_framework import status
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

@api_view(['POST'])
@parser_classes([FormParser])
def createTodo(request):
    context = TodoSerializer(data=request.data)
    if(context.is_valid()):
        context.save()
        return Response({'message': "Todo created"}, status=status.HTTP_201_CREATED)
    return Response(context.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateTodo(request):
    # convert the string to int request_data is immutable
    request_data = request.data.copy()  # deep copy deep copy is mutable
    f = {}
    for i in request_data:
        f[i] = request_data[i]
    ids = request_data['id'] #return id and pop it off
    context = Todo.objects.filter(id=ids).update(**f)
    return Response({'message': "Todo update"}, status=status.HTTP_201_CREATED)