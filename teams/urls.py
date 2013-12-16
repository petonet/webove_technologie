from django.conf.urls import patterns, include, url
from teams.models import Team
from teams import views

info_dict = {
    'queryset': Team.objects.all(),

}


urlpatterns = patterns('',
    url(r'^$', views.TeamsView.as_view()),
    url(r'^(?P<pk>\d+)/$', 'teams.views.teamDetail'),
    url(r'^new/$','teams.views.addTeam'),
    url(r'^myTeam/$','teams.views.myTeam'),
    url(r'^sendRequestForMembership/$','teams.views.sendRequestForMembership'),
    url(r'^cancelRequest/$','teams.views.cancelRequest'),
    url(r'^(?P<pk>\d+)/cancelMembership/$','teams.views.cancelMembership'),
    url(r'^(?P<pk>\d+)/editBasicInfo/$','teams.views.editBasicInfo'),
    url(r'^(?P<pk>\d+)/removeTeam/$','teams.views.deleteTeam'),
)
