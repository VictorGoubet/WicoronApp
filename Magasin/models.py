from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Produit(models.Model):
    Nom=models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    prix=models.FloatField(default=0.0)

    def __str__(self):
        return self.Nom

class Panier(models.Model):


    Produits=models.ManyToManyField(Produit,default=None,through='Panier_has_Produits',through_fields=('panier', 'produit'))
    Client = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

class Panier_has_Produits(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    quantite = models.IntegerField()


class Commande(models.Model):
    Produits=models.ManyToManyField(Produit,default=None,through='Commande_has_Produits',through_fields=('commande', 'produit'))
    Client = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Date=models.DateField(default=timezone.now() )

class Commande_has_Produits(models.Model):
    produit =  models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    

