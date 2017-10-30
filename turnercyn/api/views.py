'''
API Endpoints
'''

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CinemaSerializer
from .models import Cinema

class CreateCinemaView(generics.ListCreateAPIView):
    '''
    Defines create behavior for cinema
    '''
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def create(self, request):
        '''
        Save the POST data when creating a cinema
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

class CinemaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Defines the update and destroy behavior of the Cinema resource
    '''
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
