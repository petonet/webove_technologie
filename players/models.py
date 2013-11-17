from django.db import models
from django.contrib.auth.models import User
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class player(models.Model):
    user = models.OneToOneField(User, verbose_name='Pouzivatel')
    phone = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    photo = ProcessedImageField(upload_to='uploads/image/players', processors=[ResizeToFill(800, 600)], format='JPEG', options={'quality': 60}, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user.username




