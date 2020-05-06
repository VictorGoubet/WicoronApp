from django.shortcuts import render,redirect
from Connexion.carterepo import carte
from Connexion.models import Profil
from Magasin.models import Commande,Commande_has_Produits
import matplotlib.pyplot as plt
from WicoronApp.settings import BASE_DIR
import folium
from Connexion.carterepo import *
from django.contrib.auth.models import User
# Create your views here.

def mapUtilisateur(request):
    if(request.user.is_authenticated):
        coordonneeListe = []
        p = Profil.objects.all()
        for e in p:
            coordonneeListe.append([e.coordonneeGeoX,e.coordonneeGeoY])
        map = carte("Paris",75000,coordonneeListe)
        context = {'map': map}

        return render(request, 'Stats/Visual1.html', context)
    else:
        return redirect('home')

def mapDemande(request):
    if(request.user.is_authenticated):
        coordonneeListe = []
        map = folium.Map(location=coordonnee("Paris",75000),zoom_start=12)

        utilisateur = User.objects.all()
        for e in utilisateur:
            commandeParClient = {}
            p = Commande.objects.filter(Client = e)        
            for commandes in p:
                for articles in Commande_has_Produits.objects.filter(commande=commandes):
                    if(articles.produit not in commandeParClient.keys()):
                        commandeParClient[articles.produit.Nom] = articles.quantite
                    if(articles.produit in commandeParClient.keys()):
                        commandeParClient[articles.produit.Nom] += articles.quantite
            if(commandeParClient != {}):
                profil = Profil.objects.get(user = e)
                pop = folium.Popup(html = listeCommandeToString(e.first_name,commandeParClient))
                folium.Marker([profil.coordonneeGeoX,profil.coordonneeGeoY],popup=pop).add_to(map)
        
        context = {'map': map._repr_html_()}

        return render(request, 'Stats/Visual3.html', context)
    else:
        return redirect('home')


def listeCommandeToString(client,dic):
    output =  '<p style="white-space: nowrap;"><span><b>' +  client + "</b></span><BR>"
    for e in dic.keys():
        output += '<span>' + str(dic[e]) + " " + e + '</span><BR>'
    output += '</p>'
    return output[:-1]

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
        
        return render(request, 'Stats/Visual2.html',{"affichage":True})
    else:
        return redirect('home')

def Visual(request):
    # Page d'arriver, on choisit ici d'afficher directement la map
    return redirect('mapUtilisateur')
