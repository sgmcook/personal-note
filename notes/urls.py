from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

'''
    List of URLs an API user can provide and the views they 
    link to in views.py
'''
urlpatterns = [
    path('', views.api_root),
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)