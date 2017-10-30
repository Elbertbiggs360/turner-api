'''
Test the cinema viewpoint
'''

from rest_framework import status
from api.tests.test_basecase import APITestCase
from ..models import Cinema
from django.core.urlresolvers import reverse

class ViewCinemaTestCase(APITestCase):
    '''
    Test Suite for the cinema endpoint
    '''

    def test_api_can_create_cinema(self):
        '''
        Test api can create cinema
        '''
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_a_cinema(self):
        '''
        Test api can get a cinema
        '''
        cinema = Cinema.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': cinema.id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, cinema)

    def test_api_can_update_cinema(self):
        '''
        Test api can update cinema data
        '''
        cinema = Cinema.objects.get()
        change_cinema = {'short_name': 'CNC', 'name': 'Century Cinema, Acacia'}
        response = self.client.put(
            reverse('details', kwargs={'pk': cinema.id}),
            change_cinema,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_cinema(self):
        '''
        Test api can delete cinema
        '''
        cinema = Cinema.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': cinema.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)