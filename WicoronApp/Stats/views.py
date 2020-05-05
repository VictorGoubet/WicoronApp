from django.shortcuts import render,redirect
from Connexion.carterepo import carte
from Connexion.models import Profil
from Magasin.models import Commande,Commande_has_Produits
import matplotlib.pyplot as plt
from WicoronApp.settings import BASE_DIR
# Create your views here.

def mapUtilisateur(request):
    if(request.user.is_authenticated):
        coordonneeListe = []
        p = Profil.objects.all()
        for e in p:
            coordonneeListe.append([e.coordonneeGeoX,e.coordonneeGeoY])
        map = carte("Paris",75000,coordonneeListe)
        context = {'map': map}

        return render(request, 'Stats/Visual.html', context)
    else:
        return redirect('home')


def StatProduits(request):
    if(request.user.is_authenticated):
        commandes=Commande.objects.all()
        dictCmd={}
        for x in commandes:
            ListeProduit=x.Produits.all()
            for i in ListeProduit:
                qt=Commande_has_Produits.objects.get(produit=i,commande=x).quantite
                if(i.Nom not in dictCmd):
                    dictCmd[i.Nom ]=qt
                else:
                    dictCmd[i.Nom ]+=qt

        f = plt.figure()
        plt.title('Consommation des produits')
        plt.xlabel('Produits')
        plt.ylabel('Quantité commandée')
        plt.bar(dictCmd.keys(), dictCmd.values(),width=1.0,bottom=0,color='Green',alpha=0.65)
        plt.grid()
        plt.savefig(BASE_DIR+"/static/images/barplot.png")
        
        return render(request, 'Stats/Visual.html',{"affichage":True})
    else:
        return redirect('home')

def Visual(request):
    # Page d'arriver, on choisit ici d'afficher directement la map
    return redirect('mapUtilisateur')
