'''
Models for the application
'''

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Cinema(models.Model):
    '''
    Model definition for a Cinema
    '''
    # e.g. 'CEN'
    short_name = models.CharField(
        max_length=3, verbose_name='Cinema short name')
    # e.g. 'CENTURY'
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        verbose_name='Cinema full name')
    # Dates for creation and modification
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)

    def __str__(self):
        '''
        Returns a human readable representation of the model instance
        '''
        return u"{0} ({1})".format(self.name, self.short_name)

