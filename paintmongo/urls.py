from django.conf.urls import patterns, include, url
from paint.views import home,current_datetime,gallery,save,load

urlpatterns = patterns('',
    url('^$', home),
    url(r'^time/$', current_datetime),
    url(r'^gallery/$', gallery),
    url(r'^save/$', save),
    url(r'^gallery/([^/]+)$', load),
)
