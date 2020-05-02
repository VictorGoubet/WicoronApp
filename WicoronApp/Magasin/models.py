from django.db import models
from Connexion.forms import SignUpForm

class Produit(models.Model):
    Nom=models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    prix=models.FloatField(default=0.0)

class Panier(models.Model):

    Produits=models.ManyToManyField(Produit)
    Total=models.FloatField(default=0.0)
    #idClient = models.ForeignKey(SignUpForm, on_delete=models.SET_NULL)

