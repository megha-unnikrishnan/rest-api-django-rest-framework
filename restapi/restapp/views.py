from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers,UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(completed=True)
    serializer_class = TaskSerializers

class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(completed=False)
    serializer_class = TaskSerializers

class CreateUserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
# Create your views here.
