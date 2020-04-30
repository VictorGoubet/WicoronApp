from django.shortcuts import render

# Create your views here.

def Register(request):
    return render(request,"Connexion/signup.html")


def Login(request):
    return render(request,"Connexion/signin.html")
