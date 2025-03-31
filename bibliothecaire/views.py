from django.shortcuts import render, redirect
from .models import Membre, Media
from .forms import MembreForm, MediaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm


# Inscription
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard') # Voir plus bas pour la redirection
    else:
        form = CustomUserCreationForm()
    return render(request, 'bibliothecaire/register.html', {'form': form})

# Connexion
class CustomLoginView(LoginView):
    template_name = 'bibliothecaire/login.html'

    def get_success_url(self):
        if self.request.user.role == 'bibliothecaire':
            return '/bibliothecaire/'
        else:
            return '/membre/'

@login_required
def dashboard(request):
    if request.user.role == 'bibliothecaire' :
        return render(request, 'bibliothecaire/dashboard.html')
    return render(request, 'membre/dashboard.html')

@login_required
def dashboard_membre(request):
    return render(request, 'membres/membre_dashboard.html')

def liste_membres(request):
    membres = Membre.objects.all()
    return render (request, 'liste_membres.html', {'membres' : membres})

def ajouter_membre(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else: form = MembreForm()

    return render(request, 'ajouter_membre.html', {'form' : form})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'liste_medias.html', {'medias' : medias})

def ajouter_media(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else: form = MediaForm()


