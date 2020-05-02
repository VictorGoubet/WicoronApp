from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.

def Register(request):
    if( request.method=='POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            login(request,user)
            #Puis sign in
            return render(request,"Connexion/signin.html")
    else:
        form = SignUpForm()
    return render(request,"Connexion/signup.html")


def Login_view(request):
    if(request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return render(request,"index.html")
    return render(request,"Connexion/signin.html")

def Logout_view(request):

    logout(request)
    return redirect('home')


