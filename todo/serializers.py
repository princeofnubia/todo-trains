from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','task_name', 'is_trashed', 'task_status', 'user', 'is_archived', 'schedule_on', 'date_created', "last_updated"]
