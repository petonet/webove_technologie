from django.db import models
from players.models import player
from grounds.models import ground
from django.contrib.auth.models import User
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    startOfAction = models.DateTimeField()
    published = models.DateTimeField(auto_now_add=True, blank=True)
    numberOfPlayers = models.IntegerField()
    login_since = models.DateTimeField()
    prologue = models.CharField(max_length=1000)
    scenario = models.CharField(max_length=1000)
    organizationNotes = models.CharField(max_length=1000)
    duration = models.TimeField()
    entryFee = models.DecimalField(decimal_places=3, max_digits=5)
    locationLat = models.CharField(max_length=20, null=True, verbose_name='Latitude')
    locationLng = models.CharField(max_length=20, null=True, verbose_name='Longitude')
    users = models.ManyToManyField(player, null=True, blank=True)
    author = models.ForeignKey(User)
    ground = models.ForeignKey(ground, null=True, blank=True)
    titleImage=ProcessedImageField(upload_to='uploads/image/events',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    def __unicode__(self):
        return self.title


class Restrictions(models.Model):
    eventId = models.ForeignKey(Event)
    gunFps = models.DecimalField(decimal_places=1, max_digits=4)
    pyro = models.CharField(max_length=100)
    age = models.IntegerField()
    def __unicode__(self):
        return 'Restrictions'

class Comments(models.Model):
    eventId = models.ForeignKey(Event)
    user = models.ForeignKey(player)
    comment = models.CharField(max_length=1000)
    sent = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment


class Notifications (models.Model):
    eventId = models.ForeignKey(Event)
    content = models.CharField(max_length=100)
    def __unicode__(self):
        return self.content