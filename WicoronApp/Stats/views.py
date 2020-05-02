from django.shortcuts import render,redirect


# Create your views here.
def Visual(request):
    if(request.user.is_authenticated):
        return render(request,"Stats/Visual.html")
    else:
        return redirect('home')
