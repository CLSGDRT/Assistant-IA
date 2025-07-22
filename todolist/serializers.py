from todolist.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'completed_at']

