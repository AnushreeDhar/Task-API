from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    #queryset = Task.objects.all().order_by('date')
    model = Task
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('completed',)#filtering based on fields
    ordering = ('date',)
    search_fields = ('@task_desc',)
#class DueTaskViewSet(viewsets.ModelViewSet):

   # queryset = Task.objects.all().order_by('date').filter(completed=False)
   # serializer_class = TaskSerializer

#class CompletedTaskViewSet(viewsets.ModelViewSet):
   # queryset = Task.objects.all().order_by('date').filter(completed=True)
   # serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)


       
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,  )
    serializer_class = UserSerializer

