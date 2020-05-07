from django.db import models


# Create your models here.
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    codePostal = models.IntegerField(help_text='Code Postal')
    adresse = models.CharField(max_length=200, help_text='Adresse')
    ville = models.CharField(max_length=200, help_text='Ville')
    nbPersonne = models.IntegerField(help_text='Nombre de personne dans le foyer')
    coordonneeGeoX = models.FloatField(help_text='Coordonnée en X')
    coordonneeGeoY = models.FloatField(help_text='Coordonnée en Y')
    numero = models.CharField(max_length=10, help_text='Numere de téléphone')
    def __str__(self):
        return "Profil de {0}".format(self.user.username)