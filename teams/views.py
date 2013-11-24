from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from HrajAirsoft import settings
from django.views import generic
from HrajAirsoft.settings import PROJECT_PATH
from players.models import player
from teams.models import Team, NewsFeeds, Gallery, UserInTeamNtoN


class TeamsView(generic.ListView):
    model = Team
    template_name = 'teams\\index.html'

class TeamsDetailView(generic.ListView):
    model = Team
    template_name = 'teams\\ground_detail.html'

"""

class IndexView(generic.ListView):

    template_name = 'teams/index.html'
    context_object_name = 'teams_list'

    def get_queryset(self):
        return Team.objects.order_by('-reg_date')

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)

        for e in Team.objects.all():
            e.counts_of_players = UserInTeamNtoN(team_id=e.pk).objects.count()
            e.save()

        context['edited_team_list'] = Team.objects.order_by('-reg_date')

        return context
"""

class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'

    def get_context_data(self, **kwargs):
        a = []
        context = super(DetailView, self).get_context_data(**kwargs)
        #print 'toto je kontext id', self.kwargs.get('pk', None)
        for e in UserInTeamNtoN.objects.filter(team_id=self.kwargs.get('pk', None)):
            a.append(player.objects.filter(pk=e.user_id.user_id)[0])
        context['players'] = a

        #try:
        #    context['players'] = player(pk=UserInTeamNtoN(team_id=self.model.pk).user_id).objects.all()
        #except ValueError:
        #    print 'Error(Weak) - teams.views.DetailView - v danom time je len osoba ktora ho vytvorila'
        #    context['players'] = None

        #context['new_feeds'] = NewsFeeds(team_id=self.model.pk).objects.order_by('-publish_date')
        context['new_feeds'] = NewsFeeds.objects.filter(team_id=self.kwargs.get('pk', None))
        context['GalleryTeam'] = Gallery.objects.filter(team_id=self.kwargs.get('pk', None))
        #context['path'] = PROJECT_PATH.strip("\HrajAirsoft").replace('\\', '/') + "/"


        return context

