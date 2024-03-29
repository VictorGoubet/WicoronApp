from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    codePostal = forms.IntegerField(help_text='Code Postal')
    adresse = forms.CharField(max_length=200, help_text='Adresse')
    nbPersonne = forms.IntegerField(help_text='Nombre de personne dans le foyer')
    ville = forms.CharField(max_length=200, help_text='Ville')
    numero = forms.CharField(max_length=10, help_text='Numere de téléphone')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2','codePostal','adresse','nbPersonne','ville','numero')