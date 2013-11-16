from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}),
   url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'players/logout.html'}),
   url(r'^profile/$', 'players.views.profile'),
   )
