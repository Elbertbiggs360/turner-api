'''
URL Patterns for the API Endpoints
'''
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCinemaView, CinemaDetailsView

urlpatterns = {
    url(r'^cinemas/$', CreateCinemaView.as_view(), name='create'),
    url(r'^cinemas/(?P<pk>[0-9]+)/$', CinemaDetailsView.as_view(), name='details'),
}
urlpatterns = format_suffix_patterns(urlpatterns)
