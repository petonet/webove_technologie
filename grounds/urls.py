from django.conf.urls import patterns, include, url
from grounds import views
from models import ground



urlpatterns = patterns('',
   #url(r'^$/',views.IndexView.as_view(),name='index' ),
  url(r'^(?P<pk>\d+)/$', views.GroundDetailView.as_view(model=ground), name='detail'),
  url(r'^all/$',views.GroundsOverview.as_view(model=ground))
)
