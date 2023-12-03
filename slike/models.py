from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Galerija(models.Model):

    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = CloudinaryField('image')








