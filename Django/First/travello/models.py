from django.db import models

# Create your models here.

class Destination(models.Model):
    place = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)