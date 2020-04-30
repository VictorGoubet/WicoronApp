from django.shortcuts import render

# Create your views here.
def Visual(request):
    return render(request,"Stats/Visual.html")
