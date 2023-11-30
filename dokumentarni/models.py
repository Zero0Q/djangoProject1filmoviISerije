# Importiramo django model klasu
from django.db import models

# Definišemo klasu za TV seriju
class TVShow(models.Model):
    # Svaka TV serija ima naziv, žanr, opis i sliku
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    # image = models.ImageField(upload_to='tvshows/')

    # Metoda koja vraća naziv TV serije
    def __str__(self):
        return self.name

# Definišemo klasu za sezonu
class Season(models.Model):
    # Svaka sezona pripada nekoj TV seriji i ima broj i godinu izlaska
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='seasons')
    number = models.IntegerField()
    year = models.IntegerField()

    # Metoda koja vraća naziv sezone u formatu "TV serija - Sezona X"
    def __str__(self):
        return f'{self.tvshow.name} - Season {self.number}'

# Definišemo klasu za epizodu
class Episode(models.Model):
    # Svaka epizoda pripada nekoj sezoni i ima broj, naziv i trajanje
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    # Metoda koja vraća naziv epizode u formatu "SXXEXX - Naziv"
    def __str__(self):
        return f'S{self.season.number:02}E{self.number:02} - {self.title}'

