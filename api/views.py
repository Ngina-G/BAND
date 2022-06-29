from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NotesSerializer
from .models import Notes


class NotesViewSet(viewsets.ModelViewSet): 
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

