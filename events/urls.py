from django.conf.urls import patterns, include, url
from events import views

urlpatterns = patterns('',
    url(r'^$', views.EventsView.as_view(), name='events'),
    url(r'^new/$', 'events.views.add', name='addEvent'),
    #url(r'^maptest/$', 'events.views.MapView', name='mapTest'),
    url(r'^detail/(?P<pk>\d+)/$', 'events.views.eventDetail', name='eventDetail'),
)