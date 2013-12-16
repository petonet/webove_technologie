from django.conf.urls import patterns, include, url
from grounds.views import *
from models import ground
from django.contrib.auth.decorators import login_required




urlpatterns = patterns('',
   #url(r'^$/',views.IndexView.as_view(),name='index' ),
  url(r'add/$', login_required(GroundCreate.as_view(model=ground))),
  url(r'update/(?P<pk>\d+)$', login_required(GroundUpdate.as_view(model=ground))),
  url(r'delete/(?P<pk>\d+)$', login_required(GroundDelete.as_view(model=ground))),
  url(r'^(?P<pk>\d+)/$', GroundDetailView.as_view(model=ground), name='detail'),
  url(r'^$',GroundsOverview.as_view(model=ground))
)
