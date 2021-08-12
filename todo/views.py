from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import FormParser
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Todo


# Create your views here.
@swagger_auto_schema(
    method='put',
    request_body=IDTodoSerializer,
    responses={404: 'data not found', 200: 'trash is empty'}
)
@api_view(['PUT'])
def emptyTrash(request):
    todo = Todo.objects.all().filter(is_trashed = True).delete()
    return Response({'message': 'trash is empty'})

@swagger_auto_schema(
    method='get',
    operation_description="Get todos of a particular user that is not archived not trashed",
)
@api_view(['GET'])
def getTodos(request):
    request_data = request.data.copy()  # deep copy deep copy is mutable
    f = {}
    for i in request_data:
        f[i] = request_data[i]
    user_id = request_data['user_id']
    todo = Todo.objects.all().filter(is_trashed = False, is_archived = False, user_id=user_id)
    context =  TodoSerializer(todo, many=True)
    return Response(context.data) # response client

@swagger_auto_schema(
    method='post',
    request_body=TodoSerializer
)
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
    ids = request_data['todo_id'] #return id and pop it off
    context = Todo.objects.filter(todo_id=ids).update(**f)
    return Response({'message': "Todo update"}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def archiveTodo(request):
    # convert the string to int request_data is immutable
    request_data = request.data.copy()  # deep copy deep copy is mutable
    ids = request_data['todo_id'] #return id and pop it off
    context = Todo.objects.filter(todo_id=ids).update(is_archived = True)
    return Response({'message': "Todo archived"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getArchived(request):
    # convert the string to int request_data is immutable
    todo = Todo.objects.all().filter(is_archived=True)
    context =  TodoSerializer(todo, many=True)
    return Response(context.data)

@api_view(['GET'])
def getTrash(request):
    # convert the string to int request_data is immutable
    todo = Todo.objects.all().filter(is_trashed=True)
    context =  TodoSerializer(todo, many=True)
    return Response(context.data)

@api_view(['PUT'])
def trash(request):
    # convert the string to int request_data is immutable
    request_data = request.data.copy()  # deep copy deep copy is mutable
    ids = request_data['todo_id'] #return id and pop it off
    context = Todo.objects.filter(todo_id=ids).update(is_trashed = True, is_archived = False)
    return Response({'message': "Todo trashed"}, status=status.HTTP_201_CREATED)