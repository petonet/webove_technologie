__author__ = 'root'

from django import template
from teams.models import Team, UserInTeamNtoN

register = template.Library()


def nav_teamslist():
    teams = Team.objects.all().order_by('-name')

    for e in Team.objects.all():

        try:
            if UserInTeamNtoN.objects.filter(team_id=e.pk).count():
                e.counts_of_players = UserInTeamNtoN.objects.filter(team_id=e.pk).count()
                e.save()
            else:
                e.counts_of_players = 0
        except ValueError:
            print 'Error(Weak) - nav_teamlist - v danom time je len osoba ktora ho vytvorila'
            e.counts_of_players = 0
        finally:
            e.counts_of_players += 1
            e.save()

    return {'teams': teams}



register.inclusion_tag('tags/teams_all.html')(nav_teamslist)