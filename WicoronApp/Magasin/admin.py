from django.contrib import admin
from .models import Produit,Panier,Panier_has_Produits

# Register your models here.
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(Panier_has_Produits)

