from django.db import models
from players.models import player
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Team(models.Model):
    #2000*300
    big_logo = ProcessedImageField(upload_to='uploads/image/teams/big_logos',processors=[ResizeToFill(2000, 300)],format='JPEG',options={'quality': 60}, blank=True, null=True)
    team_logo = ProcessedImageField(upload_to='uploads/image/teams/logos',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60}, blank=True, null=True)
    leader = models.ForeignKey(player)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    reg_date = models.DateTimeField()
    counts_of_players = models.IntegerField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


    #samozrejme jeden hrac by nemal byt v dvochb timoch alebo feature uvidi sa
class UserInTeamNtoN(models.Model):

    team_id = models.ForeignKey(Team)
    user_id = models.ForeignKey(player)
    invitation = models.NullBooleanField(blank=True, null=True)
    accepted = models.NullBooleanField(blank=True, null=True)
    dateOfAdd = models.DateField(blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return 'Do timu = ' + str(self.team_id) + ', je priradeny hrac = ' + str(self.user_id)


class NewsFeeds(models.Model):

    title_image = ProcessedImageField(upload_to='uploads/image/teams/feeds/logos',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60}, blank=True, null=True)
    team_id = models.ForeignKey(Team)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3500)
    publish_date = models.DateTimeField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title


class Gallery(models.Model):

    image = ProcessedImageField(upload_to='uploads/image/teams/gallery',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    team_id = models.ForeignKey(Team,blank=True, null=True)
    news_id = models.ForeignKey(NewsFeeds,blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
       return 'Team_id = ' + str(self.team_id) + ' News_id =  ' + str(self.news_id)