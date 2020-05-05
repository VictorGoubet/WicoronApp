from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from Magasin.models import Panier
from .models import Profil
from django.contrib import messages 
from django.contrib.auth.models import User
from .carterepo import carte, coordonnee
# Create your views here.
def Register(request):
    if( request.method=='POST'):
        form = SignUpForm(request.POST)
        username = request.POST['username']
        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            adresse = form.cleaned_data["adresse"]
            codepostal = form.cleaned_data["codePostal"]
            nbPersonne = form.cleaned_data["nbPersonne"]

            ville = form.cleaned_data["ville"]
            profil = Profil(user=user, codePostal = codepostal,adresse=adresse,nbPersonne=nbPersonne,ville=ville,coordonneeGeoX=0,coordonneeGeoY=0)
            profil.save()
            basket=Panier(Client=user)
            basket.save()
            login(request,user)
            
            #Creation de la carte
            map = carte(adresse,codepostal,[coordonnee(adresse,codepostal)])

            #Ajout des boutons de validation adresse ou changement 
            boutons = """<div class="row align-center"><button class="btn btn-action" onclick="window.location.href = '/Connexion/Validation';"">Valider</button>
							
							
								
								<button class="btn btn-action" onclick="window.location.href = '/Connexion/changementAdresse';">Changer</button></div>"""
        
            context = {'map': map,'boutons':boutons}
            #retour de la page affichant une carte pour valider l'adresse
            return render(request, 'Connexion/map.html', context)
        if(request.POST["password1"]!=request.POST["password2"]):
            messages.error(request, "Les deux mots de passe ne correspondent pas.")
        
        if(User.objects.exclude(pk=form.instance.pk).filter(username=username).exists()):
            messages.error(request, "Nom d'utilisateur déjà utilisé")
        if(len(request.POST["password1"])<8):
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères")
        else:
            messages.error(request, "Le mot de passe doit contenir des chiffres et des lettres.\nIl ne doit pas être trop proche de votre nom et prénom.")
    
    return render(request,"Connexion/signup.html")

def validationAdresse(request):
    
    utilisateur = Profil.objects.get(user=request.user)

    c = coordonnee(utilisateur.adresse,utilisateur.codePostal)
    utilisateur.coordonneeGeoX = c[0]
    utilisateur.coordonneeGeoY = c[1]
    print(c[0],type(c[1]))
    utilisateur.save(force_update=True)
    print(utilisateur.coordonneeGeoX)
    return redirect("home")

def changementAdresse(request):
    if(request.method =='POST'):
        adresse = request.POST["adresse"]
        codepostal = request.POST["codePostal"]
        utilisateur = Profil.objects.get(user=request.user)
        utilisateur.adresse = adresse
        utilisateur.codepostal = codepostal
        utilisateur.ville = request.POST["ville"]
        utilisateur.save(force_update=True)

        #Creation de la carte
        map = carte(adresse,codepostal,[coordonnee(adresse,codepostal)])

        #Ajout des boutons de validation adresse ou changement 
        boutons = """<div class="row align-center"><button class="btn btn-action" onclick="window.location.href = '/Connexion/Validation';"">Valider</button>
						
						
							
							<button class="btn btn-action" onclick="window.location.href = '/Connexion/changementAdresse';">Changer</button></div>"""
    
        context = {'map': map,'boutons':boutons}
        #retour de la page affichant une carte pour valider l'adresse
        return render(request, 'Connexion/map.html', context)



    return render(request, 'Connexion/changementAdresse.html')



def Login_view(request):
    if(request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Le mot de passe est incorrect ou le compte n'existe pas *")
    return render(request,"Connexion/signin.html")

def Logout_view(request):

    logout(request)
    return redirect('home')


