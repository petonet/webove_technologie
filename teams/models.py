from django.db import models
from players.models import player
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Team(models.Model):

    team_logo = ProcessedImageField(upload_to='uploads/image/teams/logos',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    leader = models.ForeignKey(player)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    reg_date = models.DateTimeField()
    counts_of_players = models.IntegerField()


    #samozrejme jeden hrac by nemal byt v dvochb timoch alebo feature uvidi sa
class UserInTeamNtoN(models.Model):

    team_id = models.ForeignKey(Team)
    user_id = models.ForeignKey(player)


class NewsFeeds(models.Model):

    team_id = models.ForeignKey(Team)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3500)
    publish_date = models.DateTimeField()


class Gallery(models.Model):

    image = ProcessedImageField(upload_to='uploads/image/teams/gallery',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    team_id = models.ForeignKey(Team)
    news_id = models.ForeignKey(NewsFeeds)