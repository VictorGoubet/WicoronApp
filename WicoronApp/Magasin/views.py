from django.shortcuts import render,redirect
from .models import Produit,Panier,Panier_has_Produits,Commande,Commande_has_Produits
from Connexion.models import Profil

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

def StoreAllergieView(request):
    if(request.user.is_authenticated):
        return render(request,"Magasin/StoreAllergie.html")
    else:
        return redirect('home')

def PanierView(request):
    if(request.user.is_authenticated):
        msg=""
        #On récupére le panier du client
        basket=Panier.objects.get(Client=request.user)
        if( request.method=='POST'):
            n=Profil.objects.get(user=request.user).nbPersonne
            #On ajoute les produits selectionnés au panier
            for prdt in request.POST:
                if(prdt[:4]=="inpt" and int(request.POST[prdt])>0 ):
                    #On récupére l'entité produit 
                    newProduit=Produit.objects.get(Nom=prdt[5:])
                    #On verifie si le produit n'est pas déja dans le panier
                    if(newProduit not in basket.Produits.all()):
                        
                        if int(request.POST[prdt])<=n:
                            q=int(request.POST[prdt]) 
                        else:
                            q=n
                            msg="Certain produits ont été limité en quantité !"

                       
                        basket.Produits.add(newProduit,through_defaults={'quantite':q})
                    else:
                        
                        #si il est déja présent on récupére la quantité et on limite au nb de personne dans le foyer
                        liaison=Panier_has_Produits.objects.get(panier=basket,produit=newProduit)
                        if(liaison.quantite+int(request.POST[prdt])<=n):
                            liaison.quantite+=int(request.POST[prdt])
                        else:
                            liaison.quantite=int(n)
                            msg="Certain produits ont été limité en quantité !"
                        liaison.save()
        
        else:
            for info in request.GET:

                if(request.GET[info]=="pay"):
                    contenu=Panier_has_Produits.objects.filter(panier=basket).all()
                    if(len(contenu)>0):
                        #On enregistre la commande :
                        NewCommande=Commande(Client=request.user)
                        NewCommande.save()
                        #On vide le panier
                        
                        for x in contenu:
                            NewCommande.Produits.add(x.produit,through_defaults={'quantite':x.quantite})
                            x.delete()
                        NewCommande.save()
                        msg="Votre commande est passée !"
                    else:
                        msg="Il n'y a rien dans votre panier !"
                            
                    #En réalité il y aurait une autre page sur la quelle on redirgie pour le paiement

                else:
                    #On récupére le produit à supprimer :
                    prdtDel=Produit.objects.get(Nom=request.GET[info])
                    liaisonDel=Panier_has_Produits.objects.get(panier=basket,produit=prdtDel)
                    liaisonDel.delete()
                    msg="L'article a été supprimé !"


        qt=Panier_has_Produits.objects.filter(panier=basket).all()
        produitsCmd=Panier.objects.get(Client=request.user).Produits.all()
        recap=list(zip(produitsCmd,qt))
        total=0
        for p,q in recap:
            total+=p.prix*q.quantite

        return render(request,"Magasin/Panier.html",{"recap":recap,"total":round(total,2),"msg":msg})
        

    else:
        return redirect('home')