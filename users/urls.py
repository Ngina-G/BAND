from django.urls import re_path
from .views import RegisterView, LoginView, UserView, LogoutView,ProfileRetrieveAPIView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^api/register/', RegisterView.as_view()),
    re_path(r'^api/login/', LoginView.as_view()),
    re_path(r'^api/user/', UserView.as_view()),
    re_path(r'^api/profile/(?P<id>\w+)/', ProfileRetrieveAPIView.as_view()),
    re_path(r'^api/logout/', LogoutView.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
