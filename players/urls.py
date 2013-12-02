from django.conf.urls import patterns, include, url
import HrajAirsoft


urlpatterns = patterns('',
   url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}),
   url(r'^login/fail$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}),
   url(r'^changepass/$', 'players.views.changepass'),
   #url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'players/logout.html'}),
   url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'homepage/homepage.html'}),
   url(r'^profile/$', 'players.views.profile'),
   url(r'^aboutMe/$', 'players.views.aboutMe'),
   url(r'^registration/$','players.views.registration'),
   )
