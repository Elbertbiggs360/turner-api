'''
The Base Test Case for the API tests
'''

from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse

from ..models import Cinema

class ModelTestCase(TestCase):
    '''
    Test Suite for the Cinema Models
    '''

    def setUp(self):
        '''
        Define test client and other variables
        '''
        self.cinema_name = 'Century'
        self.cinema = Cinema(name=self.cinema_name)

    def tearDown(self):
        '''
        Reset settings
        '''

class APITestCase(TestCase):
    '''
    Test Suite for API Endpoints
    '''
    def setUp(self):
        '''
        Define test client
        '''
        self.client = APIClient()
        self.cinema_data = {'name': 'Century Cinema', 'short_name': 'CEN'}
        self.response = self.client.post(
            reverse('create'),
            self.cinema_data,
            format='json'
        )
