from django.db.models import query
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.serializers import Serializer
from app.serializers import UserSerializer, GroupSerializer, TaskSerializer
from app.models import Task
from rest_framework.decorators import action
from rest_framework.response import Response
from app.tasks import execute

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == "current":
            return self.request.user
        return super(UserViewSet, self).get_object()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def execute(self, request, pk=None):
        execute.delay(pk)
        return Response(data='Task running', status=status.HTTP_200_OK)
