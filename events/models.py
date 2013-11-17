from django.db import models
from players.models import player
# Create your models here.



class Event(models.Model):
    title=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    published=models.DateTimeField()
    logon_since=models.DateTimeField()
    prologue=models.CharField()
    scenario=models.CharField()
    organizationNotes=models.CharField()
    endOfAction=models.DateTimeField()
    entryFee=models.DecimalField()
    respPerson=models.ForeignKey(player)     #player ako argument ale este nie je imple
    comments=models.ForeignKey(Comments)
    restrictions=models.ForeignKey(Restrictions)



class Restrictions(models.Model):
    gunFps=models.DecimalField()
    pyro=models.CharField()
    age=models.DecimalField()

class Comments(models.Model):
    player=models.ForeignKey(player)#player ako argument ale este nie je imple
    comment=models.CharField(max_length=500)

