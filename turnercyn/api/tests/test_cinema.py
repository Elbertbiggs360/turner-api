'''
Test the cinema models
'''

from django.test import TestCase
from turnercyn.api.tests.test_basecase import ModelTestCase
from ..models import Cinema

class CinemaTestCase(ModelTestCase):
    '''
    Test Suite for the Cinema Models
    '''

    def test_model_can_create_a_cinema(self):
        '''
        Test cinema model can create a cinema
        '''
        old_count = Cinema.objects.count()
        self.cinema.save()
        new_count = Cinema.objects.count()
        self.assertNotEqual(old_count, new_count)
