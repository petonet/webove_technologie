
from django import template
from teams.models import Team, UserInTeamNtoN
from django.template.loader import add_to_builtins

register = template.Library()


def nav_teamslist():
        teams = Team.objects.all().order_by('-name')
        for e in Team.objects.all():
            e.counts_of_players = UserInTeamNtoN(team_id=e.pk).objects.count()
            e.save()
        return {'teams': teams}



register.inclusion_tag('tags/teams_all.html')(nav_teamslist)
#add_to_builtins('teams.templatetags.teams_tag')