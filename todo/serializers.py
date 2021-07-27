from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task_name', 'task_status', 'user', 'is_archived', 'schedule_on']
