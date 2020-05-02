from django.shortcuts import render,redirect
from .models import Produit

# Create your views here.
def Store(request):
    if(request.user.is_authenticated):
        produits=Produit.objects.all()
        return render(request,"Magasin/Store.html",{'prdts':produits})
    else:
        return redirect('home')

def Panier(request):
    if(request.user.is_authenticated):
        return render(request,"Magasin/Panier.html")
    else:
        return redirect('home')