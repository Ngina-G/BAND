from django.urls import re_path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    re_path(r'^api/register/', RegisterView.as_view()),
    re_path(r'^api/login/', LoginView.as_view()),
    re_path(r'^api/user/', UserView),
    re_path(r'^api/logout/', LogoutView.as_view()),
]
