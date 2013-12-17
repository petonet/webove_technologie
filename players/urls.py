from django.conf.urls import patterns, include, url
import HrajAirsoft


urlpatterns = patterns('',
   url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}),
   url(r'^login/fail$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}),
   url(r'^changepass/$', 'players.views.changepass'),
   url(r'^changephoto/$', 'players.views.changephoto'),
   #url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'players/logout.html'}),
   url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'homepage/homepage.html'}),
   url(r'^profile/$', 'players.views.profile'),
   url(r'^aboutMe/$', 'players.views.aboutMe'),
   url(r'^(?P<pk>\d+)/$', 'players.views.detail'),
   url(r'^registration/$','players.views.registration'),
   #url(r'^myTeam/$','players.views.myTeam'),
   )
