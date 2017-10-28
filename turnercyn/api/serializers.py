'''
Serializers for the models
'''

from rest_framework import serializers
from .models import Cinema

class CinemaSerializer(serializers.Serializer):
    '''
    Serializer to map cinema model into json instance
    '''
    class Meta:
        '''
        Meta class to wrap serializer fields to model fields
        '''
        model = Cinema
        fields = ('id','short_name', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
