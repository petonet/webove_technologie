from django.db import models

# Create your models here.


class topMenu(models.Model):
    menuCategory=models.CharField(max_length=100)


