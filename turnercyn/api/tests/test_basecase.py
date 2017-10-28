'''
The Base Test Case for the API tests
'''

from django.test import TestCase
from django.core.cache import cache

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
