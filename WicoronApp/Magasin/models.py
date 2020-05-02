from django.db import models

class Produit(models.Model):
    Nom=models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    prix=models.FloatField(default=0.0)

class Panier(models.Model):
    pass

