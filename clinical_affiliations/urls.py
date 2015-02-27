""" Main project urls """
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'clinical_affiliations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^$', 'communications.views.institutions', name='institutions'),
    url(r'^communications/', include('communications.urls'), name='communications'),
)
