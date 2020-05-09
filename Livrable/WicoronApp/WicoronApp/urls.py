
from django.contrib import admin
from django.urls import path, include   
from . import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Magasin/', include('Magasin.urls')),
    path('Stats/', include('Stats.urls')),
    path('Connexion/', include('Connexion.urls')),
]
