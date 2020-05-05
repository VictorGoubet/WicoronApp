from django.shortcuts import render,redirect
from Connexion.carterepo import carte
from Connexion.models import Profil
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

def Visual(request):
    # Page d'arriver, on choisit ici d'afficher directement la map
    return redirect('mapUtilisateur')
