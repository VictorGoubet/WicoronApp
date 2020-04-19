
from django.contrib import admin
from django.urls import path,include
from . import views

app_name='blog' 

urlpatterns = [

    path('', views.index,name="index"),
    path('posts/<int:id>', views.show,name='show'),


]
