'''
Test the cinema viewpoint
'''

from rest_framework import status
from api.tests.test_basecase import APITestCase

class ViewCinemaTestCase(APITestCase):
    '''
    Test Suite for the cinema endpoint
    '''

    def test_api_can_create_cinema(self):
        '''
        Test api can create cinema
        '''
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
