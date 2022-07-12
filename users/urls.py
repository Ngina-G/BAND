from django.urls import re_path
from .views import RegisterView, LoginView, UserView, LogoutView,ProfileRetrieveAPIView,NotesViewSet,NotesDelete,NotesUpdate,ProfileUpdate
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^api/register/', RegisterView.as_view()),
    re_path(r'^api/login/', LoginView.as_view()),
    re_path(r'^api/user/', UserView.as_view()),
    re_path(r'^api/profile/(?P<id>\w+)/', ProfileRetrieveAPIView.as_view()),
    re_path(r'^api/logout/', LogoutView.as_view()),
    re_path(r'^notes/$', NotesViewSet),
    re_path(r'^notes/(?P<owner_id>\w+)/', NotesViewSet),
    re_path(r'^deleteNote/(?P<NoteId>\w+)/',NotesDelete),
    re_path(r'^updateNote/(?P<NoteId>\w+)/', NotesUpdate),
    re_path(r'^updateProfile/(?P<id>\w+)/', ProfileUpdate),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
