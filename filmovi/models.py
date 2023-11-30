from django.db import models
from cloudinary.models import CloudinaryField

from django.urls import reverse

# Create your models here.
class Film(models.Model):
    ime = models.CharField(max_length=250)
    originalIme = models.CharField(max_length=120, blank=True, null=True)
    zanr = models.CharField(max_length=200)
    radnja = models.TextField(max_length=5000)
    godina = models.CharField(max_length=10)
    imdbOcena = models.CharField(max_length=100)
    linkPreuzmi = models.CharField(max_length=1000)
    linkGledaj = models.CharField(max_length=1000)
    linkPrevod = models.CharField(max_length=200, blank=True, null=True)
    # image = models.ImageField(upload_to='media/', blank=True, null=True)
    image = CloudinaryField('image')
    # image = CloudinaryField('media/')


    # sam menja url da ne mora svaki posebno
    def get_absolute_url(self):
        return f"/filmovi/{self.id}/"


    # def get_absolute_url(self):
    #     return reverse("filmovi:filmovi_detail", kwargs={'id': self.id})

    def __str__(self):
        return self.ime
