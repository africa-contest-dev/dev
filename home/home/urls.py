import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

PROJECT_ROOT = os.path.dirname(__file__)

urlpatterns = patterns('',
    url(r'^$', 'mainApp.views.homePage', name='home'),
    # url(r'^$', 'home.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PROJECT_ROOT, '../frontEnd/static')}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)