from django.db import models
import Image

# Create your models here.


class ground(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=200)
    street=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="uploads/image/grounds",width_field="image_width",height_field="image_height")
    description=models.CharField(max_length=1000)
    rate=models.PositiveIntegerField()
    official=models.BooleanField(default='false')
    pubDate=models.DateTimeField("published")




    def save(self):
        if not self.id and not self.the_image:
            return;

        image = Image.open(self.the_image)
        ratio_height = (890*self.image_height)/self.image_width
        size = (890,ratio_height)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.the_image.path)
        super(ground, self).save()

