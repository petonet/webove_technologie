from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from players.models import player
from teams.models import Team, NewsFeeds, Gallery, UserInTeamNtoN


class TeamsView(generic.ListView):
    model = Team
    template_name = 'teams\\index.html'


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


class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'

    def get_context_data(self, **kwargs):

        context = super(DetailView, self).get_context_data(**kwargs)

        context['players'] = player(pk=UserInTeamNtoN(team_id=self.model.pk).user_id).objects.all()
        context['new_feeds'] = NewsFeeds(team_id=self.model.pk).objects.order_by('-publish_date')
        context['GalleryNewFeeds'] = Gallery(news_id=NewsFeeds.pk).objects.all()
        context['GalleryTeam'] = Gallery(team_id=self.model.pk).objects.all()

        return context

