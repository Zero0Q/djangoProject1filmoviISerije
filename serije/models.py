from django.db import models


# Create your models here.
class Serija(models.Model):
    naziv = models.CharField(max_length=250)
    originalNaziv = models.CharField(max_length=120, blank=True, null=True)
    zanr = models.CharField(max_length=200)
    radnja = models.TextField(max_length=5000)
    godina = models.CharField(max_length=10)
    imdbOcena = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    # sam menja url da ne mora svaki posebno
    # def get_absolute_url(self):
    #     return f"/serije/{self.id}/"

    def __str__(self):
        return self.naziv


class Sezona(models.Model):
    serija = models.ForeignKey(Serija, on_delete=models.CASCADE, related_name='sezone')
    broj = models.IntegerField()

    def __str__(self):
        return f'{self.serija.naziv} - Season {self.broj}'


class Epizoda(models.Model):
    sezona = models.ForeignKey(Sezona, on_delete=models.CASCADE, related_name='epizode')
    broj = models.IntegerField()
    linkPreuzmi = models.CharField(max_length=1000)
    linkGledaj = models.CharField(max_length=1000)
    linkPrevod = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'S{self.sezona.broj:02}E{self.broj:02}'
