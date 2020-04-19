from django.shortcuts import render
from .models import Posts
from django.http import Http404
# Create your views here.



def index(request):
    posts=Posts.objects.all()

    return render(request,"blog/pages/index.html",{'posts':posts})


def show(request,id):
    try:
        post=Posts.objects.get(pk=id)
    except:
        raise Http404("désole cet article n'existe pas !")

    return render(request,"blog/pages/show.html", {'post':post} )
