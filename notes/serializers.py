from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    '''
        Serialize the note object + fields
        Links owner (user who created note) to notes
    '''
    class Meta:
        model = Note
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'title', 'pub_date', 'last_updated_date', 'body', 'archived']

    def update(self, instance, validated_data):
        validated_data.pop('pub_date', None)  # prevent pub_date from being updated
        return super().update(instance, validated_data)    


class UserSerializer(serializers.ModelSerializer):    
    '''
        Links notes and users with the primary key
    '''
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']