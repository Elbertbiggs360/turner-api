'''
URL Patterns for the API Endpoints
'''
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCinemaView

urlpatterns = {
    url(r'^cinemas/$', CreateCinemaView.as_view(), name='create')
}
urlpatterns = format_suffix_patterns(urlpatterns)
