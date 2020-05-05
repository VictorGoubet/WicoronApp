
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Visual,name='Visual'),
    path('visual1',views.mapUtilisateur,name="mapUtilisateur"),
    path('visual2',views.StatProduits,name="StatProduits"),
    
]
