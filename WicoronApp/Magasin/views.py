from django.shortcuts import render
from .models import Produit
# Create your views here.
def Store(request):
    produits=Produit.objects.all()
    return render(request,"Magasin/Store.html",{'prdts':produits})

def Panier(request):
    return render(request,"Magasin/Panier.html")