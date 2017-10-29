'''
API Endpoints
'''

from django.shortcuts import render
from rest_framework import generics
from .serializers import CinemaSerializer
from .models import Cinema

class CreateCinemaView(generics.ListCreateAPIView):
    '''
    Defines create behavior for API
    '''
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def perform_create(self, serializer):
        '''
        Save the POST data when creating a cinema
        '''
        serializer.save()