from django.db import models
from django.contrib.auth.models import User
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class player(models.Model):
    user = models.OneToOneField(User, verbose_name='Pouzivatel')
    phone = models.DecimalField(max_digits=9, decimal_places=0)
    photo = ProcessedImageField(upload_to='uploads/image/players',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=35)


    #def __unicode__(self):
    #    return self.user.username



