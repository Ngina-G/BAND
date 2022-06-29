from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NotesSerializer, UserSerializer
from .models import Notes
from django.shortcuts import render


class NotesViewSet(viewsets.ModelViewSet): 
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

def index(request, path=''):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ReadOnly, )