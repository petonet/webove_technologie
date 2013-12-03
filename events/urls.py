from django.conf.urls import patterns, include, url
from models import Event
from events import views

urlpatterns = patterns('',
   #url(r'^$/',views.IndexView.as_view(),name='index' ),
   url(r'^$', views.EventsView.as_view(), name='events'),
   url(r'^new/$', 'events.views.add', name='addEvent'),
   url(r'^detail/(?P<pk>\d+)/$', views.EventDetailView.as_view(model=Event), name='eventDetail'),
)