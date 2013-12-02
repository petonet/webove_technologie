# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class player(models.Model):
    user = models.OneToOneField(User, verbose_name='Pouzivatel')
    phone = models.CharField(max_length=30, blank=True, null=True)
    photo = ProcessedImageField(upload_to='uploads/image/players', processors=[ResizeToFill(800, 600)], format='JPEG', options={'quality': 60}, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=80, blank=True, null=True)
    date_of_birth = models.DateField()
    rank = models.DecimalField(max_digits=9, decimal_places=0,blank=True, null=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user.username


    PRESOV = u'Pre\u0161ovsk\xfd'
    KOSICE = u'Ko\u0161ick\xfd'
    BRATISLAVA =  u'Bratislavsk\xfd'
    NITRA = u'Nitriansky'
    ZILINA =  u'\u017dilinsk\xfd'
    TRENCIN = u'Tren\u010diansky'
    TRNAVA = u'Trnavsk\xfd'
    BANSKABYSTRICA = u'Banskobystrick\xfd'
    CZ = u'Zahrani\u010die - \u010cesk\xe1 Republika'
    INE = u'Zahrani\u010die - In\xe9'

    MALE = u'Mu\u017e'
    FEMALE = u'\u017dena'

    GENDER_CHOICES = (
        (MALE, u'Mu\u017e'),
        (FEMALE, u'\u017dena'),
    )
    KRAJE_CHOICES = (
        (PRESOV, u'Pre\u0161ovsk\xfd'),
        (KOSICE, u'Ko\u0161ick\xfd'),
        (BRATISLAVA, u'Bratislavsk\xfd'),
        (NITRA,  u'Nitriansky'),
        (ZILINA, u'\u017dilinsk\xfd'),
        (TRENCIN, u'Tren\u010diansky'),
        (TRNAVA, u'Trnavsk\xfd'),
        (BANSKABYSTRICA, u'Banskobystrick\xfd'),
        (CZ, u'Zahrani\u010die - \u010cesk\xe1 Republika'),
        (INE,  u'Zahrani\u010die - In\xe9'),
    )

    about_me = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15,
                                      choices=GENDER_CHOICES,
                                      default=MALE)
    countryPart = models.CharField(max_length=60,
                                      choices=KRAJE_CHOICES,
                                      default=KOSICE)




class Armory(models.Model):
    user_id = models.ForeignKey(player)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = ProcessedImageField(upload_to='uploads/image/armory', processors=[ResizeToFill(800, 600)], format='JPEG', options={'quality': 60}, blank=True, null=True)

