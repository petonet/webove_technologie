from django.db import models
from players.models import player
# Create your models here.

class Restrictions(models.Model):
    #eventId = models.OneToOneField(Event, verbose_name='event', primary_key=True)
    #eventId = models.ForeignKey(Event)
    gunFps=models.DecimalField(decimal_places=1, max_digits=4)
    pyro=models.CharField(max_length=100)
    age=models.DecimalField(decimal_places=0, max_digits=3)



class Event(models.Model):
    title=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    published=models.DateTimeField()
    logon_since=models.DateTimeField()
    prologue=models.CharField(max_length=1000)
    scenario=models.CharField(max_length=1000)
    organizationNotes=models.CharField(max_length=1000)
    endOfAction=models.DateTimeField()
    entryFee=models.DecimalField(decimal_places=2, max_digits=5)
    respPerson=models.ForeignKey(player)
    #comments=models.ForeignKey(Comments)
    #restrictions=models.ForeignKey(Restrictions)
    #notifications=models.ForeignKey(Notifications)

class Comments(models.Model):
    eventId = models.ForeignKey(Event)
    player=models.ForeignKey(player )
    comment=models.CharField(max_length=500)

class Notifications (models.Model):

    content = models.CharField(max_length=100)
    eventId = models.ForeignKey(Event)