from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_membre(request):
    return render(request, 'membres/membre_dashboard.html')

def accueil(request):
    return render(request, "accueil.html")

def connexion(request):
    if request.method == "POST" :
        username = request.POST ['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == "bibliothecaire":
                return
            redirect('bibliothecaire:dashboard')
        elif user.role == "membre":
            return
        redirect('membres:dashboard')
    else:
        return render(request, 'accueil.html',{'error' : "Identification incorrecte"})
    return render(request, 'accueil.html')