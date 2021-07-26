from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
    IN_PROGRESS='in-progress'
    DONE='done'
    TODO='todo'
    task_status=[(IN_PROGRESS,'in-progress'), (DONE,'done'),(TODO,'todo')]
    task_name = models.CharField(max_length=50)
    task_status =models.CharField(max_length=15, choices=task_status,default=TODO)
    is_trashed=models.BooleanField(default=False)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created=models.DateField()
    last_updated=models.DateField()
    is_archived=models.BooleanField(default=False)
    schedule_on=models.DateField()