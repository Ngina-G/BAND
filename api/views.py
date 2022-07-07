from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NotesSerializer
from .models import Notes
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def NotesViewSet(request,id=0):
  if request.method=='GET':
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)
  elif request.method=='POST':
        notes_data=JSONParser().parse(request)
        notes_serializer = NotesSerializer(data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
  elif request.method=='PUT':
        notes_data = JSONParser().parse(request)
        notes=Notes.objects.get(DepartmentId=notes_data['id'])
        notes_serializer=NotesSerializer(notes,data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
  elif request.method=='DELETE':
        notes=Notes.objects.get(id=id)
        notes.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)