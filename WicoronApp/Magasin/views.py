from django.shortcuts import render
from .models import Produit

# Create your views here.
def Store(request):
    if(request.user.is_authenticated):
        produits=Produit.objects.all()
        return render(request,"Magasin/Store.html",{'prdts':produits})
    else:
        pass

def Panier(request):
    return render(request,"Magasin/Panier.html")