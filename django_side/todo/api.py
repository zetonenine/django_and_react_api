from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializers


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializers
