from django.db import models
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from players import models as player
import datetime
from django.contrib.auth.models import User

# Create your models here.


class ground(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    rate=models.PositiveIntegerField(default=2.5)
    official=models.BooleanField(default='false')
    pubDate=models.DateTimeField("published",default=datetime.datetime.now())
    photo = ProcessedImageField(upload_to='uploads/image/grounds',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})
    user =models.ForeignKey(User)





    #def save(self):
    #    if not self.id and not self.photo:
    #        return;
    #
    #    image = Image.open(self.photo)
    #    ratio_height = (890*self.photo.height)/self.photo.width
    #    size = (890,ratio_height)
    #    image = image.resize(size, Image.ANTIALIAS)
    #    image.save(self.photo.path)
    #    super(ground, self).save()

