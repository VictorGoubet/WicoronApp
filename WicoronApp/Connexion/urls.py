
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('Login',views.Login,name='Login'),
    path('Register',views.Register,name='Register'),
    
]
