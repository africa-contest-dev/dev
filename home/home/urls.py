import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

PROJECT_ROOT = os.path.dirname(__file__)

urlpatterns = patterns('',
    url(r'^$', 'mainApp.views.landingPage', name='landing-home'),
     # url(r'^landing/(?P<page_number>\w+)', 'mainApp.views.landing'),
    url(r'^home/$', 'mainApp.views.homePage', name='home'),
    url(r'^home/(?P<country_code>\w+)/$', 'mainApp.views.countryPage'),
    url(r'^about/$', 'mainApp.views.aboutPage', name='about'),
    url(r'^contact/$', 'mainApp.views.contactPage', name='contact'),
    url(r'^apply/$', 'mainApp.views.applyPage', name='apply'),
    url(r'^constitution/$', 'mainApp.views.view_Constitution', name='constitution'),
    # url(r'^$', 'home.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PROJECT_ROOT, 'static')}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)