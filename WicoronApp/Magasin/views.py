from django.shortcuts import render,redirect
from .models import Produit,Panier

import logging
import pprint
pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger("PrinterInfo")

# Create your views here.
def StoreView(request):
    if(request.user.is_authenticated):
        produits=Produit.objects.all()
        return render(request,"Magasin/Store.html",{'prdts':produits})
    else:
        return redirect('home')

def PanierView(request):
    logger.info("dictionnaire :")
    if( request.method=='POST'):

        #On ajoute les produits selectionnés au panier
        for prdt in request.POST:
            if(prdt[:4]=="inpt" and int(request.POST[prdt])>0 ):
                basket=Panier.objects.get(Client=request.user)
                if(basket!=None):
                    newProduit=Produit.objects.get(Nom=prdt[5:])
                    basket.Produits.add(newProduit)
            
        produitsCmd=Panier.objects.get(Client=request.user).Produits.all()
        if(request.user.is_authenticated):
            return render(request,"Magasin/Panier.html",{"prdts":produitsCmd})
        else:
            return redirect('home')