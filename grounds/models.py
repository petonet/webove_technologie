from django.db import models
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.


class ground(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=200)
    street=models.CharField(max_length=200)
    #photo=models.ImageField(upload_to="uploads/image/grounds",blank=True)
    description=models.CharField(max_length=1000)
    rate=models.PositiveIntegerField()
    official=models.BooleanField(default='false')
    pubDate=models.DateTimeField("published")
    photo = ProcessedImageField(upload_to='uploads/image/grounds',processors=[ResizeToFill(800, 600)],format='JPEG',options={'quality': 60})






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

