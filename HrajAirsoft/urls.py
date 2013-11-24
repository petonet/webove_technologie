from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import grounds
import players
from grounds import urls
from home import views as homeViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HrajAirsoft.views.home', name='home'),
    # url(r'^HrajAirsoft/', include('HrajAirsoft.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     #ground detail
      url(r'^grounds/', include('grounds.urls')),
      url(r'^events/', include('events.urls')),
      url(r'^$',homeViews.HomeView.as_view()),
      url(r'^accounts/', include('players.urls')),
      url(r'^teams/', include('teams.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)