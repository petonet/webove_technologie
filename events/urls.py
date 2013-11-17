from django.conf.urls import patterns, include, url
from events import views



urlpatterns = patterns('',
   #url(r'^$/',views.IndexView.as_view(),name='index' ),
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)
