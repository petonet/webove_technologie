from django.conf.urls import patterns, include, url
from events import views

urlpatterns = patterns('',
   #url(r'^$/',views.IndexView.as_view(),name='index' ),
   url(r'^$', views.EventsView.as_view(), name='events'),
   url(r'^new/$', views.EventsView.as_view(), name='createEvent'),
   url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)