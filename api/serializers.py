from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'notes']

        
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')