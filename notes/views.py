from notes.models import *
from notes.serializers import *
from notes.permissions import *

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    '''
        Default page if the person provides no object path
        or Token
    '''
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):
    '''
        When URL = localhost:PORT/users/
        Lists all users if access token is valid
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''
        When URL = localhost:PORT/users/<id>
        Lists a user and their notes if access token is valid
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteList(generics.ListCreateAPIView):
    '''
        When URL = localhost:PORT/notes/
        Lists all notes of the user associated with the JWT
    '''
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should only return notes for the logged in user
        and allows a filter query on "archived"
        """
        user = self.request.user
        queryset = Note.objects.filter(owner=user)
        
        archived = self.request.query_params.get('archived')
        
        if archived is not None:
            archived = archived.capitalize()
            queryset = queryset.filter(archived=archived)
        
        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        When URL = localhost:PORT/notes/<id>
        Lists a note if access token is valid
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer