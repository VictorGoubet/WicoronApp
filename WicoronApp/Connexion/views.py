from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.

def Register(request):
    if( request.method=='POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()

            #Puis sign in
            return render(request,"Connexion/signin.html")
    else:
        form = SignUpForm()
    return render(request,"Connexion/signup.html")


def Login(request):
    return render(request,"Connexion/signin.html")
