'''
Test the cinema models
'''

from django.test import TestCase
from api.tests.test_basecase import ModelTestCase
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

    def test_model_has_right_attributes(self):
        '''
        Test cinema model has all the attributes of cinema
        '''
        cinema_data = {"short_name": "MGC", "name": "Cinema Magic"}
        cinema = Cinema(
            short_name=cinema_data['short_name'],
            name=cinema_data['name'])
        cinema.save()
        new_cinema = Cinema.objects.get(short_name="MGC")
        self.assertEqual(cinema_data['name'], new_cinema.name)
