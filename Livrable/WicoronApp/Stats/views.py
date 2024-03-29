from django.shortcuts import render,redirect
from Connexion.carterepo import carte
from Connexion.models import Profil
from Magasin.models import Commande,Commande_has_Produits

#import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import pandas as pd

from WicoronApp.settings import BASE_DIR
import folium
from folium import plugins
from folium.plugins import HeatMap
from Connexion.carterepo import *
from django.contrib.auth.models import User
# Create your views here.



def heatmapDemande(request):
    if(request.user.is_authenticated):
        listecmd=Commande.objects.all()
        coordoneListe=[(cmd.cX,cmd.cY) for cmd in listecmd ]
        data=[]
        for k in range(len(coordoneListe)) :#On ajoute les coordonnées de chaque commande à notre liste Data sous forme normalisée
            l=[]
            l.append(coordoneListe[k][0])
            l.append(coordoneListe[k][1])
            l.append(k)
            data.append(l)

        m = folium.Map([48, 5], tiles='stamentoner', zoom_start=5)#On créer une map Folium


        #Creation de la Heatmap
        HeatMap(data,gradient={0.2: "green", 0.5: "yellow", 0.8: "red"},radius = 35   ).add_to(folium.FeatureGroup(name='Heat Map',).add_to(m))

                               

        folium.LayerControl().add_to(m)


        return render(request,'Stats/Visual4.html',{'map':m._repr_html_()})
    else:
        return redirect('home')

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
        map = folium.Map(location=coordonnee("Vesdun",18360),zoom_start=5.5)

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


        data=pd.DataFrame( data={ 'produits':list(dictCmd.keys()),'quantité':list(dictCmd.values()) } )

        fig = px.bar(data, x='produits', y='quantité',
             hover_data=['produits', 'quantité'], color='quantité',
             height=500)

        graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
        
        
        return render(request, 'Stats/Visual2.html',{"barplot":graph_div})
    else:
        return redirect('home')





def Visual(request):
    # Page d'arriver, on choisit ici d'afficher directement la map
    return redirect('heatmapDemande')
