from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notes.views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'note', NoteList, basename='Note')
router.register(r'user', UserList, basename='User')


urlpatterns = [
    path('', include('notes.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
