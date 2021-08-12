from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['todo_id','task_name', 'is_trashed', 'task_status', 'user', 'is_archived', 'schedule_on', 'date_created', "last_updated"]

class CreateTodoSerializer(TodoSerializer):
    class Meta:
        model = Todo
        fields = ['task_name', 'task_status', 'user', 'schedule_on']


class UpdateTodoSerializer(TodoSerializer):
    class Meta:
        model = Todo
        fields = ['todo_id','task_name', 'is_trashed', 'task_status','is_archived', 'schedule_on']

class IDTodoSerializer(TodoSerializer):
    class Meta:
        model = Todo
        fields = ('todo_id',)