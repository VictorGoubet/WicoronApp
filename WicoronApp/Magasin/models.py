from django.db import models

from django.contrib.auth.models import User

class Produit(models.Model):
    Nom=models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    prix=models.FloatField(default=0.0)

class Panier(models.Model):

    Produits=models.ManyToManyField(Produit,default=None,through='Panier_has_Produits',through_fields=('panier', 'produit'))
    Total=models.FloatField(default=0.0)
    Client = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

class Panier_has_Produits(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    quantite=models.FloatField(default=0)
    

