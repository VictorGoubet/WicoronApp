
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Visual,name='Visual'),
    path('visual1',views.mapUtilisateur,name="mapUtilisateur"),
    path('visual2',views.StatProduits,name="StatProduits"),
    path('visual3',views.mapDemande,name="mapDemande"),
    path('visual4',views.heatmapDemande,name="heatmapDemande"),
    
]
