from django.conf.urls import patterns, include, url
from teams.models import Team
from teams import views

info_dict = {
    'queryset': Team.objects.all(),

}


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
