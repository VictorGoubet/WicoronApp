
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('/Store',views.Store,name='Store'),
    path('/Panier',views.Panier,name='Panier'),
]
