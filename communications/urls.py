""" Communications urls """
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    'communications',
    url(r'^institutions.html$', views.institutions, name='institutions'),
    url(r'^institutions/(?P<institution_id>[0-9]+)$', views.institution, name='institution'),
    url(r'^contact/(?P<contact_id>[0-9]+)$', views.contact, name='contact'),
)
