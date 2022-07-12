from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer,ProfileSerializer,NotesSerializer
from .models import User,Profile,Notes
import jwt, datetime
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets,status
from .renderers import ProfileJSONRenderer
from rest_framework.generics import RetrieveAPIView,CreateAPIView
from rest_framework.permissions import AllowAny
from .exceptions import ProfileDoesNotExist
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
class RegisterView(CreateAPIView):
        model = User.objects.all()
        permission_classes = [permissions.AllowAny]
        serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
# def serialize_user(user):
#     return {
#         "username": user.username,
#         "email": user.email,
#     }

# @api_view(['GET'])
# def UserView(request):
#     user = request.user
#     if user.is_authenticated:
#         return Response({
#             'user_data': serialize_user(user)
#         })
#     return Response({})

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ProfileRetrieveAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get(self, request, id, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(
                user__id=id
            )
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
@csrf_exempt
def ProfileUpdate(request,id):
    if request.method=='PUT':
        profile = Profile.objects.get(user_id=id) 
        profile_data = JSONParser().parse(request)      
        profile_serializer=ProfileSerializer(profile,data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse(profile_serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

@csrf_exempt
def NotesViewSet(request,owner_id=0): 
  if request.method=='GET':
    queryset = Notes.objects.filter(owner_id=owner_id).all()
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
        notes=Notes.objects.get(NoteId=notes_data)
        notes_serializer=NotesSerializer(notes,data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
@csrf_exempt
def NotesDelete(request,NoteId):
  if request.method=='DELETE':
        notes=Notes.objects.get(NoteId=NoteId)
        notes.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def NotesUpdate(request,NoteId): 
      try: 
        notes = Notes.objects.get(NoteId=NoteId) 
      except Notes.DoesNotExist: 
        return JsonResponse({'message': 'The Note does not exist'}, status=status.HTTP_404_NOT_FOUND) 

      if request.method=='PUT':
        notes_data = JSONParser().parse(request)      
        notes_serializer=NotesSerializer(notes,data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse(notes_serializer.errors,status=status.HTTP_404_NOT_FOUND)

    # @csrf_exempt
    # def NotesAdd(request): 
    #     if request.method=='POST':
    #         notes_data=JSONParser().parse(request)  
    #         notes_serializer = NotesSerializer(data=notes_data)
    #         if notes_serializer.is_valid(): 
    #             notes_serializer.save()
    #             return JsonResponse("Added Successfully!!" , safe=False)
    #         return JsonResponse("Failed to Add.",safe=False)