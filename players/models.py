from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class player(models.Model):
    user = models.OneToOneField(User, verbose_name='Pouzivatel')
    phone = models.DecimalField(max_digits=9, decimal_places=0)
    photo = models.ImageField(upload_to="uploads/image/grounds",blank=True)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=35)


    def __unicode__(self):
        return self.user.username


    def save(self):
        if not self.id and not self.photo:
            return;

        image = Image.open(self.photo)
        ratio_height = (890*self.photo.height)/self.photo.width
        size = (890,ratio_height)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)
        super(player, self).save()

