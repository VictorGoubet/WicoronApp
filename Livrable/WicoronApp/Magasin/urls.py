
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('Store',views.StoreView,name='Store'),
    path('StoreAllergie',views.StoreAllergieView,name='StoreAllergie'),
    path('Panier',views.PanierView,name='Panier'),
]
