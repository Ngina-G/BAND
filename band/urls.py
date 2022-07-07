from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('notes/', views.NotesViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
