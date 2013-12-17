from django.conf.urls import patterns, include, url
from events import views

urlpatterns = patterns('',
    url(r'^$', 'events.views.eventList', name='eventList'),
    url(r'^new/$','events.views.add', name='addEvent'),
    url(r'^detail/(?P<pk>\d+)/$', 'events.views.eventDetail', name='eventDetail'),
)