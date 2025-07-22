from rest_framework import permissions, viewsets
from todolist.models import Task
from todolist.serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('id')

        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)