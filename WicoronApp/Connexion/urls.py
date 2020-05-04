
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('Login',views.Login_view,name='Login'),
    path('Register',views.Register,name='Register'),
    path('Logout',views.Logout_view,name='Logout'),
    path('Validation',views.validationAdresse,name='Validation'),
    
]
