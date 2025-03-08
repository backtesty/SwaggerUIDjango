from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    schema = AutoSchema(
        tags=['Tasks'],
        component_name='Task',
        operation_id_base='Task'
    )
    